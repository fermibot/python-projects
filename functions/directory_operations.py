import os


def NotebookDirectory():
    _filePath = os.path.abspath(__file__)
    return _filePath


def NotebookFileName():
    _filePath = os.path.abspath(__file__)
    return _filePath


def Import(fileName:str):
    pass