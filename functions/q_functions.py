def _promptReal():
    print("Input needs to be a real number \nDie Eingabe muss eine reelle Zahl sein")


def ListQ(_obj):
    return isinstance(_obj, list) or isinstance(_obj, range)


def MatrixQ(_list: list):
    if allListQ(_list):
        _matrixQ = True
        for i in _list:
            _matrixQ = _matrixQ and not allListQ(i)
        return _matrixQ
    elif not allListQ(_list):
        return False


def allListQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and ListQ(i)
    return _truth


def someListQ(_list: list):
    _truth = False
    for i in _list:
        _truth = _truth or ListQ(i)
    return _truth


def TupleQ(_obj):
    return isinstance(_obj, tuple)


def allTuple(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and TupleQ(i)
    return _truth


def IntegerQ(_obj):
    return isinstance(_obj, int)


def allIntegerQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and IntegerQ(i)
    return _truth


def FloatQ(_obj):
    return isinstance(_obj, float)


def allFLoatQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and FloatQ(i)
    return _truth


def NumberQ(_obj):
    return isinstance(_obj, float) or isinstance(_obj, int)


def allNumberQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and NumberQ(i)
    return _truth


def StringQ(_obj):
    return isinstance(_obj, str)


def allStringQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and StringQ(i)
    return _truth


def MemberQ(_list: list, obj):
    try:
        return obj in _list
    except TypeError:
        print("The first argument must be list and second one a possible member type.")
        print("Das erste Argument muss in der Liste stehen und das zweite muss ein möglicher Elementtyp sein.")


def allMemberQ(_list: list):
    _truth = True
    for i in _list:
        _truth = _truth and i
    return _truth


def _round(x: float):
    try:
        if x % int(x) < 0.5:
            return int(x)
        elif x % int(x) >= 0.5:
            return int(x) + 1
    except TypeError:
        _promptReal()


def EvenQ(_number):
    _number = _round(_number)
    if _number % 2 == 0:
        return True
    else:
        return False


def OddQ(_number):
    return not EvenQ(_number)


def Negative(_obj):
    def _negativeHelp(__obj):
        try:
            if NumberQ(__obj):
                if __obj < 0:
                    return True
                elif __obj >= 0:
                    return False
        except TypeError:
            return ""

    if NumberQ(_obj):
        return _negativeHelp(_obj)

    elif ListQ(_obj):
        _negative = []
        for i in _obj:
            _negative.append(_negativeHelp(i))
        return _negative


def NonNegative(_obj):
    def _nonNegativeHelp(__obj):
        try:
            if NumberQ(__obj):
                if __obj >= 0:
                    return True
                elif __obj < 0:
                    return False
        except TypeError:
            return ""

    if NumberQ(_obj):
        return _nonNegativeHelp(_obj)

    elif ListQ(_obj):
        _nonNegative = []
        for i in _obj:
            _nonNegative.append(_nonNegativeHelp(i))
        return _nonNegative


def Positive(_obj):
    def _positiveHelp(__obj):
        try:
            if NumberQ(__obj):
                if __obj > 0:
                    return True
                elif __obj <= 0:
                    return False
        except TypeError:
            return ""

    if NumberQ(_obj):
        return _positiveHelp(_obj)

    elif ListQ(_obj):
        _positive = []
        for i in _obj:
            _positive.append(_positiveHelp(i))
        return _positive


def NonPositive(_obj):
    def _nonPositiveHelp(__obj):
        try:
            if NumberQ(__obj):
                if __obj <= 0:
                    return True
                elif __obj > 0:
                    return False
        except TypeError:
            return ""

    if NumberQ(_obj):
        return _nonPositiveHelp(_obj)

    elif ListQ(_obj):
        _nonPositive = []
        for i in _obj:
            _nonPositive.append(_nonPositiveHelp(i))
        return _nonPositive


# Contains
def containedInAllQ(_obj, _list):
    _containedInAllQ = True
    for i in _list:
        _containedInAllQ = MemberQ(i, _obj) and _containedInAllQ
    return _containedInAllQ


def ContainsNone():
    pass


def ConatainsAny():
    pass


def ContainsExactly():
    pass


def ContainsOnly():
    pass


def IntersectingQ(*args):
    _intersection = []
    for i in args[0][0]:
        if containedInAllQ(i, args[0]):
            _intersection.append(i)
        else:
            _intersection = _intersection
    if len(_intersection) != 0:
        return True
    else:
        return False


def DisjointQ(*args):
    return not IntersectingQ(args)


def UniqueAllQ(_list: list):
    def _union(_list: list):
        __union = []
        for i in _list:
            if i not in __union:
                __union.append(i)
        return __union
    return len(_list) == len(_union(_list))
