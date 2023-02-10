from .mathematical_functions import *


def Total(_list: list):
    _total = float(0)
    for i in _list:
        _total += i
    return _total


def Mean(_list: list):
    return Total(_list) / len(_list)


def SampleMean(_sample: list):
    return Total(_sample) / (len(_sample) - 1)


def Variance(_sample: list):
    _mean = Mean(_sample)
    _squaredErrors = []
    for i in _sample:
        _squaredErrors.append((_mean - i) ** 2)
    return SampleMean(_squaredErrors)


def StandardDeviation(_sample: list):
    _mean = Mean(_sample)
    _squaredErrors = []
    for i in _sample:
        _squaredErrors.append((_mean - i) ** 2)
    return SampleMean(_squaredErrors) ** 0.5


def Skewness(_sample: list):
    _mean = Mean(_sample)
    _cubedErrors = []
    for i in _sample:
        _cubedErrors.append((_mean - i) ** 3)
    return SampleMean(_cubedErrors) / (Variance(_sample) ** 1.5)


def Kurtosis(_sample: list):
    _mean = Mean(_sample)
    _kurtedErrors = []
    for i in _sample:
        _kurtedErrors.append((_mean - i) ** 4)
    return SampleMean(_kurtedErrors) / (Variance(_sample) ** 2)


def NormalDistributionPDF(x, mu: float=0, sigma: float=1):
    _pi = Pi()
    _E = E()
    _factor = 1 / Sqrt(2 * _pi * (sigma ** 2))
    _exponent = ((x - mu) ** 2) / (2 * (sigma ** 2))
    return _factor * (_E ** (-_exponent))


def NormalDistributionCDF(x, mu: float=0, sigma: float=1):
    return 0.5 * (1 + Erf((x - mu) / (sigma * Sqrt(2))))


def NormalDistributionInverseCDF(x):
    _x = x
    [a1, a2, a3, a4] = [2.50662823884, -18.61500062529, 41.39119773534, -25.44106049637]
    [b1, b2, b3, b4] = [-8.47351093090, 23.08336743743, -21.06224101826, 3.13082909833]
    [c1, c2, c3, c4] = [0.3374754822726147, 0.9761690190917186, 0.1607979714918209, 0.0276438810333863]
    [c5, c6, c7, c8] = [0.0038405729373609, 0.0003951896511919, 0.0000321767881768, 0.0000002888167364]
    c9 = 0.0000003960315187

    if _x < 0 or _x > 1:
        return OverflowError

    elif 0.08 < _x < 0.92:
        _y = _x - 0.5
        _z = _y ** 2
        _num = a1 + (a2 * _z) + (a3 * (_z**2)) + (a4 * (_z**3))
        _den = 1 + (b1 * _z) + (b2 * (_z**2)) + (b3 * (_z**3)) + (b4 * (_z**4))
        return _y * _num / _den

    elif (0 <= _x <= 0.08) or (0.92 >= _x >= 1):

        _y = _x - 0.5
        if _y <= 0:
            _z = _x
        elif _y > 0:
            _z = 1 - _x

        _k = LogE(-LogE(_z))
        _preInv = (c1 + (c2 * _k) + (c3 * (_k**2)) + (c4 * (_k**3)) + (c5 * (_k**4)) + (c6 * (_k**5))
                   + (c7 * (_k**6)) + (c8 * (_k**7)) + (c9 * (_k**9)))

        if _y >= 0:
            return _preInv
        elif _y < 0:
            return -_preInv


def BinomialDistributionPDF(_n, _p, _x):
    if 0 < _p < 1:
        _x = Round(_x)
        if 0 <= _x <= _n:
            return binomial(_n, _x) * (_p ** _x) * ((1 - _p) ** (_n - _x))
        elif _x < 0 or _x > _n:
            return 0
    elif _p >= 1 or _p <= 0:
        return "Probability needs to be between 0 and 1 \n Die Wahrscheinlichkeit muss zwischen 0 und 1 liegen"
