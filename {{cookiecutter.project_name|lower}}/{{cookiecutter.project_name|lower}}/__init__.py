from os import path

def get_path():
    return path.abspath(path.dirname(path.dirname(__file__)))

