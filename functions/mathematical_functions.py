from .precision import *


def Gamma(x):
    return x


def Sin(x: float):
    _sin = 0
    _Pi = Pi(100)
    x = x % _Pi
    for i in range(50):
        _sin += (((-1)**i) * (x**((2 * i) + 1)) / (factorial((2 * i) + 1)))
    return _sin


def Cos(x: float):
    _cos = 0
    _Pi = Pi(100)
    x = x % _Pi
    for i in range(50):
        _cos += (((-1)**i) * (x**(2 * i)) / (factorial(2 * i)))
    return _cos


def Tan(x: float):
    _cos = Cos(x)
    if _cos == 0:
        return None
    else:
        return Sin(x) / Cos(x)


def Sec(x):
    _cos = Cos(x)
    if _cos == 0:
        return None
    else:
        return 1 / _cos


def Csc(x):
    _sin = Sin(x)
    if _sin == 0:
        return None
    else:
        return 1 / Sin(x)


def Cot(x):
    _sin = Sin(x)
    if _sin == 0:
        return None
    else:
        return Cos(x) / _sin


def ArcSin(x: float):
    _arcsin = []
    for i in range(50):
        _arcsin += ((factorial(2 * i)) * (x ** ((2 * i) + 1)) / ((4 ** i) * ((factorial(i)) ** 2) * (2 * i + 1)))


def ArcCos(x):
    return x


def ArcTan(x: float):
    _arctan = []
    for i in range(50):
        _arctan += (((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1))
    return _arctan


def Erf(x):
    _erf = 0
    if x == 0:
        return _erf
    elif x != 0:
        _e = E()
        _pi = Pi()
        for i in range2(0, x, 0.001):
            _erf += (_e ** (- (i ** 2))) * 0.001
        return 2 * _erf / Sqrt(_pi)


def LogE(_x, _n=E()):
    _log = 0
    for i in range2(1, _x, 0.001):
        _log += 0.001 * 1 / i
    return _log


def Log10(_x):
    return LogE(_x) / LogE(10)


def Log(_x, _base):
    return LogE(_x) / LogE(_base)
