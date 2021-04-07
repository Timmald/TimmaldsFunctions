import os


def bytesFromPath(path: str) -> bytes:
    """
    Gets the bytes of the file at `path`

    Parameters
    -----------
    **path**(`str`): The path to the file. If it leads to a directory, it will recur through the directory until it finds a file, then return the bytes of that file

    Returns
    --------
    The bytes of the file contained in `path`
    """
    try:
        with open(path, "rb") as f:
            lines = f.read()
        return lines
    except IsADirectoryError:
        for file in os.listdir(path):
            return bytesFromPath(path + '/' + file)
