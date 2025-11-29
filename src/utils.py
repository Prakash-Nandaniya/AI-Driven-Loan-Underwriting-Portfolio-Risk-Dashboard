import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {path}")
    else:
        print(f"File not found: {path}")