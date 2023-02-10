from .q_functions import *


def print2(_obj):
    print(_obj)


def max2(_list: list):
    _max = _list[0]
    for i in _list:
        if i > _max:
            _max = i
        else:
            _max = _max
    return _max


def Min(_list: list):
    _min = _list[0]
    for i in _list:
        if i < _min:
            _min = i
        else:
            _min = _min
    return _min


def prompt_real():
    print("Input needs to be a real number \nDie Eingabe muss eine reelle Zahl sein")


def Abs(x: float):
    try:
        if x >= 0:
            _x = x
        elif x <= 0:
            _x = -1 * x
        return _x
    except TypeError:
        prompt_real()
        # TODO: This prints a redundant none statement.


def Sign(_x):
    if _x < 0:
        return -1
    elif _x > 0:
        return 1


def greater(_list):
    if len(_list) == 2:
        return _list[0] > _list[1]
    elif len(_list) > 2:
        _greater = True
        for i in range(0, len(_list)):
            _greater = _greater and (_list[i] > _list[i + 1])
            return _greater


def greater_equal(_list):
    if len(_list) == 2:
        return _list[0] >= _list[1]
    elif len(_list) > 2:
        _greaterEqual = True
        for i in range(0, len(_list)):
            _greaterEqual = _greaterEqual and (_list[i] >= _list[i + 1])
            return _greaterEqual


def less(_list):
    if len(_list) == 2:
        return _list[0] < _list[1]
    elif len(_list) > 2:
        _less = True
        for i in range(0, len(_list)):
            _less = _less and (_list[i] < _list[i + 1])
            return _less


def LessEqual(_list):
    if len(_list) == 2:
        return _list[0] <= _list[1]
    elif len(_list) > 2:
        _lessEqual = True
        for i in range(0, len(_list)):
            _lessEqual = _lessEqual and (_list[i] >= _list[i + 1])
            return _lessEqual


def less_than_all(element, _list: list):
    _truth = True
    for i in _list:
        _truth = (element < i) and _truth
    return _truth


def less_than_equal_all(element, _list: list):
    _truth = True
    for i in _list:
        _truth = (element <= i) and _truth
    return _truth


def greater_than_all(element, _list: list):
    _truth = True
    for i in _list:
        _truth = (element > i) and _truth
    return _truth


def greater_than_equal_all(element, _list: list):
    _truth = True
    for i in _list:
        _truth = (element >= i) and _truth
    return _truth


def equal_all(_list: list):
    _truth = True
    for i in range(0, _list.__len__() - 1):
        _truth = _truth and (_list[i] == _list[i + 1])
    return _truth


def range2(i, j=None, step=None):
    def _Range(_lower, _upper, _step):
        __elem, __list = _lower, []
        while True:
            __list.append(__elem)
            __elem += _step
            if __elem >= _upper:
                break
        return __list

    if step is None:
        if j is None:
            if i <= 0:
                return 0
            elif i >= 1:
                return _Range(1, i, 1)
        elif j is not None:
            if j < i:
                print("Upper limit needs to be smaller than the lower limit.")
            elif i == j:
                return i
            elif i < j:
                return _Range(i, j, 1)
    elif step is not None:
        diff = j - i
        if diff < 0:
            print("Upper limit needs to be smaller than the lower limit.")
        elif diff == 0:
            return i
        elif diff > 0:
            return _Range(i, j, step)


def factorial(x):
    if x == 0:
        return 1
    if (not isinstance(x, int)) or (x < 1):
        return "Non integer functionality not yet included"
    elif (isinstance(x, int)) and (x >= 1):
        if x == 0:
            result = 1
        elif x > 0:
            result = x * factorial(x - 1)
    return result


def factorial2(x):
    _factorial2 = 1
    if x == 0:
        return _factorial2
    elif EvenQ(x):
        for i in range(1, int(x / 2) + 1):
            _factorial2 = _factorial2 * i * 2
    elif OddQ(x):
        for i in range(1, int((x + 1) / 2) + 1):
            _factorial2 *= (2 * i - 1)
    return _factorial2


def binomial(_n, _m):
    _n, _m = Abs(_n), Abs(_m)
    return factorial(_n) / (factorial(_n - _m) * factorial(_m))


def boole(_obj):
    if _obj:
        return 1
    elif not _obj:
        return 0


def xor(bit1, bit2):
    if (bit1 and bit2) or (not bit1 and not bit2):
        return False
    else:
        return True
