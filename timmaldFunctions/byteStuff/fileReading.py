import os


def bytesFromPath(path:str):
    try:
        with open(path,"rb") as f:
            lines = f.read()
        return lines
    except IsADirectoryError:
        for file in os.listdir(path):
            return bytesFromPath(path+'/'+file)