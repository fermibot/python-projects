

def ConstructFileName(_list: list, _type: str='.txt'):
    _filePath = ''
    for i in _list:
        _filePath += i + '\\'
    _filePath = _filePath[:-1]
    _filePath += _type
    return _filePath
