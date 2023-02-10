import random


def Mean(*args: float):
    a = 0
    for i in args:
        a += i
    return a / len(args)


def sample_size_limit():
    return "The sample size needs to be greater zero"


def RandomReal(a: float = None, b: float = None, sampleSize: int = None):
    def _randomReal(_a: float = None, _b: float = None):
        if a is None and b is None:
            return random.random()
        elif (a is not None) and (b is None):
            return a * random.random()
        elif (a is None) and (b is not None):
            return b * random.random()
        elif (a is not None) and (b is not None):
            if a == b:
                return a
            elif a != b:
                _min = min([a, b])
                _max = max([a, b])
                return _min + (_max - _min) * random.random()

    if sampleSize is None:
        return _randomReal(a, b)
    elif sampleSize is not None:
        _randomSample = []
        for i in range(0, sampleSize):
            _randomSample.append(_randomReal(a, b))


def RandomInteger(a: int = None, b: int = None, sample_size: int = None):
    def __RandomInteger(_a: int = None, _b: int = None):
        if (_a is None) and (_b is None):
            return random.randint(0, 1)
        elif (_a is not None) and (_b is None):
            if _a < 0:
                return random.randint(_a, 0)
            elif _a >= 0:
                return random.randint(0, _a)
        elif (_a is not None) and (_b is not None):
            if _a == _b:
                return _a
            if _a < _b:
                return random.randint(_a, _b)
            if _a > _b:
                return random.randint(_a, _b)

    if sample_size is None:
        return __RandomInteger(a, b)
    if sample_size is not None:
        if sample_size <= 0:
            print(sample_size_limit())
        if sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(__RandomInteger(a, b))
            return sample


def UniformDistribution(a: float = None, b: float = None, sample_size: int = 1):
    def __UniformDistribution(_a: float = None, _b: float = None):
        if (_a is None) and (_b is None):
            return random.uniform(0, 1)
        elif (_a is not None) and (_b is None):
            if _a < 0:
                return random.uniform(_a, 0)
            if _a >= 0:
                return random.uniform(0, _a)
        elif (_a is None) and (_b is not None):
            if _b < 0:
                return random.uniform(_b, 0)
            if _b >= 0:
                return random.uniform(0, _b)
        elif (_a is not None) and (_b is not None):
            if _a < _b:
                return random.uniform(_a, _b)
            elif _a >= _b:
                return random.uniform(_b, _a)

    if sample_size == 1:
        return __UniformDistribution(a, b)
    elif sample_size < 1:
        return __UniformDistribution(a, b)
    elif sample_size > 1:
        sample = []
        for i in range(0, sample_size):
            sample.append(__UniformDistribution(a, b))
        return sample


def TriangularDistribution(low: float, high: float, mode: float = None, sample_size: int = 1):
    def __TriangularDistribution(_low: float, _high: float, _mode: float):
        if _mode is None:
            return random.triangular(_low, _high, Mean(_low, _high))
        if mode is not None:
            return random.triangular(_low, _high, _mode)

    if sample_size == 1:
        return __TriangularDistribution(low, high, mode)
    elif sample_size > 1:
        sample = []
        for i in range(0, sample_size):
            sample.append(__TriangularDistribution(low, high, mode))
        return sample
    elif sample_size <= 0:
        print(sample_size_limit())


def BetaDistribution(a: float = 0, b: float = 0, sample_size: int = None):
    if sample_size is None:
        if (a <= 0) or (b <= 0):
            print("Both the parameters of the Beta Distribution need to be greater than 0")
        else:
            return random.betavariate(a, b)
    elif sample_size is not None:
        if sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.betavariate(a, b))
            return sample
        elif sample_size <= 0:
            print(sample_size_limit())


def GammaDistribution(a: float = 0, b: float = 0, sample_size: int = None):
    if (a <= 0) or (b <= 0):
        print("Both the parameters of the Gamma Distribution need to be greater than 0")
    elif (a > 0) and (b > 0):
        if sample_size == 1:
            return random.gammavariate(a, b)
        elif sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.gammavariate(a, b))
            return sample
        elif sample_size < 0:
            print(sample_size_limit())


def LogNormalDistribution(a: float = 0, b: float = 0, sample_size: int = 1):
    if (a <= 0) or (b <= 0):
        print("Both the parameters of the Log-Normal Distribution need to be greater than 0")
    elif (a > 0) and (b > 0):
        if sample_size == 1:
            return random.lognormvariate(a, b)
        elif sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.lognormvariate(a, b))
            return sample
        elif sample_size < 0:
            print(sample_size_limit())


def WeibullDistribution(a: float = 0, b: float = 0, sample_size: int = 1):
    if (a <= 0) or (b <= 0):
        print("Both the parameters of the Log-Normal Distribution need to be greater than 0")
    elif (a > 0) and (b > 0):
        if sample_size == 1:
            return random.weibullvariate(a, b)
        elif sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.weibullvariate(a, b))
            return sample
        elif sample_size < 0:
            print(sample_size_limit())


def ExponentialDistribution(parameter: float = 1, sample_size: int = 1):
    if parameter <= 0:
        print("Enter a parameter value greater than one.")
    elif parameter > 0:
        if sample_size == 1:
            return random.expovariate(parameter)
        elif sample_size > 1:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.expovariate(parameter))
            return sample
        elif sample_size < 1:
            print(sample_size_limit())


def NormalDistribution(mu: float = 0, sigma: float = 1, sample_size: int = 1):
    if sigma <= 0:
        print("Sigma needs to be greater than 0.")
    elif sigma > 0:
        if sample_size == 1:
            return random.normalvariate(mu, sigma)
        elif sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.normalvariate(mu, sigma))
            return sample
        elif sample_size < 0:
            print(sample_size_limit())


def VonMisesDistribution(mu: float = 0, kappa: float = 1, sample_size: int = 1):
    if kappa <= 0:
        print("Sigma needs to be greater than 0.")
    elif kappa > 0:
        if sample_size == 1:
            return random.vonmisesvariate(mu, kappa)
        elif sample_size > 0:
            sample = []
            for i in range(0, sample_size):
                sample.append(random.vonmisesvariate(mu, kappa))
            return sample
        elif sample_size < 0:
            print(sample_size_limit())


def RandomChoice(sequence: list, sample_size: int = None):
    if sample_size is None:
        return random.choice(sequence)
    elif sample_size is not None:
        a = []
        for i in range(0, sample_size):
            a.append(random.choice(sequence))
        return a


def RandomSample(sequence: list, sample_size: int = 1):
    if sample_size >= 1:
        return random.sample(sequence, sample_size)
    elif sample_size < 1:
        print(sample_size_limit())
