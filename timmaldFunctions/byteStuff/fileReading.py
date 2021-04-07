import os


def bytesFromPath(path: str) -> bytes:
    """
    Args:
        path:A string representing the path of the file to get bytes from. If it is a path to a directory, will recur through the directory tree and return the bytes of the first file it finds.
    Returns:
        The bytes of a file indicated by the path
    """
    try:
        with open(path, "rb") as f:
            lines = f.read()
        return lines
    except IsADirectoryError:
        for file in os.listdir(path):
            return bytesFromPath(path + '/' + file)
