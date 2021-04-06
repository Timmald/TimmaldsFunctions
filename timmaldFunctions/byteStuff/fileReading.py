def bytesFromPath(path:str):
    with open(path,"rb") as f:
        lines = f.read()
        print(lines)