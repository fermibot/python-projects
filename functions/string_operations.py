from .precision import *


def StringLength(_string: str):
    return len(_string)


def StringJoin(*args):
    def _subStringJoin(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = ""
            for _i in obj:
                _stringList += str(_i)
            return _stringList

    if len(args) == 1:
        return _subStringJoin(args[0])
    elif len(args) > 1:
        _stringJoin = []
        for i in args:
            _stringJoin.append(_subStringJoin(i))
        return _stringJoin


def StringJoinBuffer(_list: list, _buffer: str = ""):
    _stringJoinBuffer = ""
    for i in range(0, len(_list) - 1):
        _stringJoinBuffer += _list[i] + _buffer
    return _stringJoinBuffer + _list[-1]


def ToString(*args):
    def _subToString(obj):
        if not ListQ(obj):
            return str(obj)
        elif ListQ(obj):
            _stringList = []
            for _i in obj:
                _stringList.append(str(_i))
            return _stringList

    if len(args) == 1:
        return _subToString(args[0])
    elif len(args) > 1:
        _toString = []
        for i in args:
            _toString.append(_subToString(i))
        return _toString


def ToUpperCase(*args):
    if (len(args) == 1) and StringQ(args[0]):
        (args[0]).upper()
    elif len(args) > 1:
        _toUpperCase = []
        for i in args:
            _toUpperCase.append(i.upper())
        return _toUpperCase


def ToLowerCase(*args):
    if (len(args) == 1) and StringQ(args[0]):
        return args[0].lower()
    elif len(args) > 1:
        _toLowerCase = []
        for i in args:
            _toLowerCase.append(i.lower())
        return _toLowerCase


def StringPadLeft(_str, *args):
    pass


def StringPadRight(_str, *args):
    pass


def Alphabet():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']


def Characters(_string: str):
    _characters = []
    for i in _string:
        _characters.append(i)
    return _characters


def StringRiffle(*args):
    # TODO: generalize this one to make sure the StringJoin Buffer becomes obsolete
    if len(args) == 1 and ListQ(args[0]) and not allListQ(args[0]):
        _stringRiffle = ""
        for i in args[0]:
            _stringRiffle += ToString(i) + " "
        return _stringRiffle
    if len(args) == 2 and ListQ(args[0]) and not ListQ(args[1]):
        _stringRiffle = ""
        for i in args[0]:
            _stringRiffle += ToString(i) + args[1]
        return _stringRiffle
    if len(args) == 2 and ListQ(args[0]) and ListQ(args[1]) and len(args[1]) == 3:
        _stringRiffle = args[1][0]
        for i in args[0]:
            _stringRiffle += i + args[1][1]
        _stringRiffle += args[1][2]
        return _stringRiffle
    if allListQ(args[0]) and len(args) == 1:
        _stringRiffle = ""
        for i in args[0]:
            for j in i:
                _stringRiffle += ToString(j) + " "
            _stringRiffle += "\n"
        return _stringRiffle
    if allListQ(args[0]) and len(args) == 3:
        _stringRiffle = ""
        for i in args[0]:
            for j in i:
                _stringRiffle += ToString(j) + args[2]
            _stringRiffle += args[1]
        return _stringRiffle


def StringRepeat(*args):
    if len(args) == 2 and StringQ(args[0]) and NumberQ(args[1]):
        _string = args[0]
        _stringRepeat = ""
        for i in range(0, Round(args[1])):
            _stringRepeat += _string
        return _stringRepeat
    elif len(args) == 3 and StringQ(args[0]) and NumberQ(args[1]) and NumberQ(args[2]):
        n = 0
        _string = args[0]
        _stringRepeat = ""

        while n <= Round(args[1] and StringLength(_stringRepeat) < Round(args[2])):
            _stringRepeat += _string
            n += 1
        return _stringRepeat


def StringDelete(*args):
    if len(args) == 2:
        if allStringQ(args):
            return args[0].replace(args[1], "")
        elif StringQ(args[0]) and ListQ(args[1]):
            _stringDelete = args[0]
            for _patterns in args[1]:
                _stringDelete = _stringDelete.replace(_patterns, "")
            return _stringDelete
