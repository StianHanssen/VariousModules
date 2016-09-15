import os


def getPath(fileName):
    return os.path.dirname(os.path.abspath(__file__)) + "\\" + fileName

def FileToString(fileName):
    with open(getPath(fileName), 'r') as myfile:
        data = myfile.read()
        return data

print(FileToString("data.txt").replace('\n', ''))
