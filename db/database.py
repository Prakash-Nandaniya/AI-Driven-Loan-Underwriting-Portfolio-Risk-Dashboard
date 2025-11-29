import pyodbc
import pandas as pd
import threading


class Database:
    def __init__(self, server, database, timeout=300):
        self.server = server
        self.database = database
        self.conn = None
        self.timeout = timeout          
        self._close_timer = None
        self._lock = threading.Lock()


    def _kill_running_timer(self):
        """Only stop the running timer. Does NOT close DB."""
        with self._lock:
            if self._close_timer:
                self._close_timer.cancel()
                self._close_timer = None


    def _connect(self):
        """Create connection if not already active."""
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            'Trusted_Connection=yes;'
            'TrustServerCertificate=yes;'
        )


    def close(self):
        """Close connection and cancel any timers."""
        with self._lock:
            if self._close_timer:
                self._close_timer.cancel()
                self._close_timer = None
            if self.conn:
                try:
                    self.conn.close()
                except Exception:
                    pass
                finally:
                    self.conn = None


    def _ensure_connection(self):
        """Ensure there's an open connection.Kill any existing timer so the DB won't auto-close while a new request is happening."""
        self._kill_running_timer()
        if self.conn is None:
            self._connect()


    def _schedule_close(self):
        """Start a new timer to close the connection after inactivity."""
        with self._lock:
            if self._close_timer:
                self._close_timer.cancel()
            self._close_timer = threading.Timer(self.timeout, self.close)
            self._close_timer.daemon = True
            self._close_timer.start()


    def fetch(self, query):
        """Execute SELECT query and return DataFrame."""
        self._ensure_connection()
        df = pd.read_sql(query, self.conn)
        self._schedule_close()
        return df
    
    
    def get_columns(self, table_name):
        self._ensure_connection()
        cursor = self.conn.cursor()
        cursor.execute(f"""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{table_name}'
            ORDER BY ORDINAL_POSITION
        """)
        return [row[0] for row in cursor.fetchall()]


    def execute(self, sql, params=None):
        """Execute INSERT/UPDATE/DELETE."""
        self._ensure_connection()
        cur = self.conn.cursor()
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        self.conn.commit()
        cur.close()
        self._schedule_close()

    