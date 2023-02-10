from .mathematical_functions import *
from .monitoring import *
from random import randrange


def dotHelp(_list1: list, _list2: list):
    if len(_list1) == len(_list2):
        product = 0
        for _i in range(0, len(_list1)):
            product += _list1[_i] * _list2[_i]
        return product
    elif len(_list1) != len(_list2):
        return vectorEqualityMessage


def promptNotIterable():
    print("The object needs to be iterable\nDas object ist nicht iterierbar")


def Head(obj):
    return type(obj)


def First(_list: list):
    try:
        return _list[0]
    except TypeError:
        promptNotIterable()


def Last(_list: list):
    try:
        _len = len(_list)
        return _list[_len - 1]
    except TypeError:
        promptNotIterable()


def Length(_list: list):
    return len(_list)


def _longestSubList(_list: list):
    _max = Length(_list[0])
    for i in _list:
        if Length(i) > _max:
            _max = Length(i)
        else:
            _max = _max
    return _max


def _shortestSubList(_list):
    _min = Length(_list[0])
    for i in _list:
        if Length(i) < _min:
            _min = Length(i)
        else:
            _min = _min
    return _min


def arrayGenerator(_list: list, n: int):
    _arrayGenerator = []
    for i in range(0, n):
        _arrayGenerator.append(_list)
    return _arrayGenerator


def findCenter(n):  # finds the center of a list with either odd or even number of elements
    if OddQ(n):
        return n // 2
    elif EvenQ(n):
        return n // 2 - 1


def Union(*args):
    _union = []
    for i in args:
        for j in i:
            if j not in _union:
                _union.append(j)
            elif i in _union:
                _union = _union
    return _union


def Join(*args):
    _join = []
    for i in args:
        for j in i:
            _join.append(j)
    return _join


def Catenate(_list: list):
    _catenate = []
    for i in _list:
        for j in i:
            _catenate.append(j)
    return _catenate


def Rest(_list: list):
    try:
        return _list[1:_list.__len__()]
    except TypeError:
        promptNotIterable()


def Total(_list: list):
    _total = 0
    for i in _list:
        _total += i
    return _total


def Accumulate(_list: list):
    _accumulate = [First(_list)]
    _element = First(_list)
    for i in range(1, Length(_list)):
        _element += _list[i]
        _accumulate.append(_element)
    return _accumulate


def Reverse(obj):
    if isinstance(obj, str):
        _obj = ""
        for i in reversed(obj):
            _obj += i
        return _obj
    elif isinstance(obj, list):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
        return _obj
    elif isinstance(obj, tuple):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
    elif isinstance(obj, range):
        _obj = []
        for i in reversed(obj):
            _obj.append(i)
        return _obj

    # else (not isinstance(obj, str)) or (not isinstance(obj, list)) or (not isinstance(obj, tuple)):
    else:
        promptNotIterable()


def Transpose(_list: list):
    _transpose = []
    for i in range(0, len(_list[0])):
        _transposelet = []
        for j in range(0, len(_list)):
            _transposelet.append(_list[j][i])
        _transpose.append(_transposelet)
    return _transpose


def Partition(_list: list, n):
    if n >= len(_list):
        return _list

    elif n < len(_list):
        _partition = []
        _partitionn = []
        i = 0
        while i < (len(_list) - (len(_list) % n)):
            for r in range(i, i + n):
                _partitionn.append(_list[r])
            _partition.append(_partitionn)
            _partitionn = []
            i += n
        return _partition


def ArrayReshape(_list: list, _reshape: list):
    _length = Length(_list)
    for i in Reverse(_reshape):
        _list = Partition(_list, _length * int(Reciprocal(i)))
    return _list


def Tuples(_list: list, level: int):
    _l = len(_list)
    _tuple = []
    for n in range(0, level):
        _tuplet = []
        for j in range(0, _l ** n):
            _tuplett = []
            for r in range(0, _l):
                _tuplettt = []
                for k in range(0, _l ** (level - n - 1)):
                    _tuplettt += [_list[r]]
                _tuplett += _tuplettt
            _tuplet += _tuplett
        _tuple.append(_tuplet)
    _tuple = Transpose(_tuple)
    return _tuple


def Permutations(_list: list, *args):
    if len(args) == 0:
        _len = len(_list)
    else:
        _len = args[0]

    _prePermutations = Tuples(_list, _len)
    _permutations = []

    for i in _prePermutations:
        if UniqueAllQ(i):
            _permutations.append(i)

    return sorted(Union(_permutations))


def Table(obj):
    # Add functionality to the function ;)
    return obj


def PowerRange(*args):
    if len(args) == 1:
        _powerRange = []
        if NumberQ(args[0]):
            i = 0
            while (10 ** i) <= args[0]:
                _powerRange.append(10 ** i)
                i += 1
            return _powerRange

    elif len(args) == 2:
        i = 0
        _powerRange = []
        while (10 ** i) <= args[1]:
            if (10 ** i >= args[0]) and (10 ** i <= args[1]):
                _powerRange.append(10 ** i)
                i += 1
            else:
                i += 1
        return _powerRange
    elif len(args) == 3:
        i = 0
        _powerRange = []
        while (args[2] ** i) <= args[1]:
            if (args[2] ** i >= args[0]) and (args[2] ** i <= args[1]):
                _powerRange.append(args[2] ** i)
                i += 1
            else:
                i += 1
        return _powerRange


def CirclePoints(*args):
    try:
        _Pi = Pi()
        if len(args) == 1:
            _circlePoints = []
            for i in range(0, args[0] + 1):
                _circlePoints.append([Sin(2 * i * _Pi / args[0]), Cos(2 * i * _Pi / args[0])])
            return _circlePoints
        elif len(args) == 2 and NumberQ(args[0]):
            _circlePoints = []
            for i in range(0, args[1] + 1):
                _circlePoints.append([args[0] * Sin(2 * i * _Pi / args[1]), args[0] * Cos(2 * i * _Pi / args[1])])
            return _circlePoints
        elif len(args) == 2 and ListQ(args[0]):
            _circlePoints = []
            for i in range(0, args[1] + 1):
                _circlePoints.append([
                    args[0][0] * Sin(((2 * i * _Pi) + args[0][1]) / args[1]),
                    args[0][0] * Cos(((2 * i * _Pi) + args[0][1]) / args[1])
                ])
            return _circlePoints
        elif len(args) == 3 \
                and ListQ(args[0]) \
                and ListQ(args[1]) \
                and NumberQ(args[1][0]) \
                and NumberQ(args[1][1]) \
                and IntegerQ(args[2]):
            _circlePoints = []
            for i in range(0, args[2] + 1):
                _circlePoints.append([
                    (args[1][0] * Sin(((2 * i * _Pi) + args[1][1]) / args[2])) + args[0][0],
                    (args[1][1] * Cos(((2 * i * _Pi) + args[1][1]) / args[2])) + args[0][1]
                ])
            return _circlePoints
    except TypeError:
        # Add documentation.
        pass


def Subdivide(*args):
    if len(args) == 1:
        try:
            if IntegerQ(args[0]) and args[0] >= 1:
                _subDivide = []
                for i in range(0, args[0] + 1):
                    _subDivide.append(i / args[0])
                return _subDivide
        except TypeError:
            print("Enter an integer value")
    elif len(args) == 2:
        try:
            if NumberQ(args[0]) and IntegerQ(args[1]) and args[1] >= 1:
                _subDivide = []
                for i in range(0, args[1] + 1):
                    _subDivide.append(i * args[0] / args[1])
                return _subDivide
        except TypeError:
            print("Enter proper arguments")
    elif len(args) == 3:
        try:
            if NumberQ(args[0]) \
                    and NumberQ(args[1]) \
                    and IntegerQ(args[2]) and args[2] >= 1:
                _subDivide = []
                for i in range(0, args[2] + 1):
                    _subDivide.append(args[0] + (i * (args[1] - args[0]) / args[2]))
                return _subDivide
        except TypeError:
            print("")


def FindDivisions(*args):
    if len(args) == 2:
        try:
            if ListQ(args[0]) and (len(args[0]) == 2) and IntegerQ(args[1]):
                pass
            elif ListQ(args[0]) and (len(args[0]) == 3) and IntegerQ(args[1]):
                pass
            elif ListQ(args[0]) and ListQ(args[1]):
                pass
            elif ListQ(args[0]) and ListQ(args[1]) and ListQ(Last(args[0])):
                pass
        except TypeError:
            pass
    else:
        pass
        # I do not understand what 'Nice Numbers' & Need to re-write the whole function.


def _padSimpleLeft(_list: list, _padding, _element):
    __padSimpleLeft = []
    if _padding > len(_list):
        for i in range(0, _padding - len(_list)):
            __padSimpleLeft.append(_element)
        return Join(__padSimpleLeft, _list)
    elif len(_list) == _padding:
        return _list
    elif _padding < len(_list):
        return _list[len(_list) - _padding: len(_list):]


def PadLeft(*args):
    if len(args) == 2 and ListQ(args[0]) and not ListQ(args[1]) and NumberQ(args[1]):
        return _padSimpleLeft(args[0], args[1], 0)
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and not ListQ(args[2]):
        return _padSimpleLeft(args[0], args[1], args[2])
    elif len(args) == 3 and NumberQ(args[1]) and ListQ(args[2]):
        if len(args[0]) >= args[1]:
            return _padSimpleLeft(args[0], args[1], "")
        elif len(args[0]) < args[1]:
            _leftPad = []
            for i in range(0, args[1] - len(args[0])):
                _leftPad.append(args[2][i % len(args[2])])
            return Join(_leftPad, args[0])
    elif len(args) == 4 and NumberQ(args[1]) and NumberQ(args[3]):
        if len(args[0]) >= args[1] + args[3]:
            return _padSimpleLeft(args[0], args[1], "")
        elif len(args[0]) < args[1] + args[3]:
            _margin = []
            for i in range(0, args[3]):
                _margin.append(args[2])
            _notMargin = []
            for i in range(0, args[1] - args[3] - len(args[0])):
                _notMargin.append(args[2])
            return Join(_notMargin, args[0], _margin)
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass
    elif len(args) == 1 and ListQ(args[0]):
        _max = _longestSubList(args[0])
        _padLeft = []
        for i in args[0]:
            _padLeft.append(_padSimpleLeft(i, _max, 0))
        return _padLeft


def _padSimpleRight(_list: list, _padding, _element):
    if len(_list) >= _padding:
        __padSimpleRight = []
        for i in range(0, _padding):
            __padSimpleRight.append(_list[i])
        return __padSimpleRight
    elif len(_list) < _padding:
        for i in range(0, _padding - len(_list)):
            _list.append(_element)
        return _list


def PadRight(*args):
    if len(args) == 2 and ListQ(args[0]) and NumberQ(args[1]):
        return _padSimpleRight(args[0], args[1], 0)
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and not ListQ(args[2]):
        return _padSimpleRight(args[0], args[1], args[2])
    elif len(args) == 3 and ListQ(args[0]) and ListQ(args[2]) and NumberQ(args[1]):
        if len(args[0]) >= args[1]:
            return _padSimpleRight(args[0], args[1], "")
        elif len(args[0]) < args[1]:
            for i in range(0, args[1] - len(args[0])):
                args[0].append(args[2][i % len(args[2])])
            return args[0]
    elif len(args) == 4 and ListQ(args[0]) and NumberQ(args[1]) and NumberQ(args[3]):
        if len(args[0]) >= args[1] + args[3]:
            return _padSimpleRight(args[0], args[1], "")
        elif len(args[0]) < args[1] + args[3]:
            _margin = []
            for i in range(0, args[3]):
                _margin.append(args[2])
            for i in range(0, args[1] - args[3] - len(args[0])):
                args[0].append(args[2])
            return Join(_margin, args[0])
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass
    elif len(args) == 1 and ListQ(args[0]):
        _max = _longestSubList(args[0])
        _padRight = []
        for i in args[0]:
            _padRight._padSimpleRight(i, _max, 0)
        return _padRight


def Fibonacci(n):
    _a = 0
    _b = 1
    _i = 1
    while _i < n:
        _temp = _b
        _b += _a
        _a = _temp
        _i += 1
    return _b


def Tribonacci(n):
    _a = 0
    _b = 0
    _c = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _c = _c + _b + _a
        _a = _temp1
        _b = _temp2
        _i += 1
    return _c


def Quadranacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _d = _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _i += 1
    return _d


def Pentonacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 0
    _e = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _temp4 = _e
        _e = _e + _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _d = _temp4
        _i += 1
    return _e


def Hexonacci(n):
    _a = 0
    _b = 0
    _c = 0
    _d = 0
    _e = 0
    _f = 1
    _i = 1
    while _i < n:
        _temp1 = _b
        _temp2 = _c
        _temp3 = _d
        _temp4 = _e
        _temp5 = _f
        _f = _f + _e + _d + _c + _b + _a
        _a = _temp1
        _b = _temp2
        _c = _temp3
        _d = _temp4
        _e = _temp5
        _i += 1
    return _f


def Polynacci(n: int, base: int):
    _polynacci = [1]
    for i in range(0, base):
        _polynacci.append(2 ** i)
    if n <= base:
        return _polynacci[n - 1]
    elif n > base:
        _len = len(_polynacci)
        while _len < n + 1:
            _polynacci.pop(0)
            _polynacci.append(Total(_polynacci))
            _len += 1
        return _polynacci[-1]


def Riffle(*args):
    # Todo: Vardhan will check and see what is the issue with this one
    # Todo: To understand, he will look at Mathematica documentation
    if len(args) == 2:
        if ListQ(args[0]) and not ListQ(args[1]):
            _riffle = []
            for i in args[0]:
                _riffle.append(i)
                _riffle.append(args[1])
            _riffle.pop((len(_riffle) - 1))
            return _riffle
        elif ListQ(args[0]) and ListQ(args[1]):
            _riffle = []
            _len = len(args[1])
            for i in range(0, len(args[0])):
                _riffle.append(args[0][i])
                _riffle.append(args[1][i % _len])
            _riffle.pop(len(_riffle) - 1)
            return _riffle

    elif len(args) == 3:
        if ListQ(args[0]) and NumberQ(args[2]):
            _riffle = []
            for i in range(len(args[0])):
                _riffle.append(args[0][i])
                pass
        elif ListQ(args[0]) and ListQ(args[2]):
            pass
    else:
        pass


def Binlists(*args):
    if len(args) == 1:
        _max = max2(args[0])
        _min = Min(args[0])
        _binLists = [_min, _max]
        return _binLists


def Append(_list, _element):
    _list.append(_element)
    return _list


def Prepend(_list, _element):
    _list.insert(0, _element)
    return _list


# Distances

vectorEqualityMessage = "Length of both the vectors needs to be the same. \n" \
                        "Die Länge beider Vektoren muss gleich sein. \n" \
                        "రెండు వెక్టర్స్ ఒకే పొడవు ఉండాలి."


def ManhattanDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        _manhattanDistance = 0
        for i in range(0, len(_vector1)):
            _manhattanDistance += Abs(_vector1[i] - _vector2[i])
        return _manhattanDistance
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def SquaredEuclideanDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        _squaredEuclideanDistance = 0
        for i in range(0, len(_vector1)):
            _squaredEuclideanDistance += Abs(_vector1[i] - _vector2[i]) ** 2
        return _squaredEuclideanDistance
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def EuclideanDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        return Sqrt(SquaredEuclideanDistance(_vector1, _vector2))
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def ChessboardDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector1):
        _chessboardDistanceList = []
        for i in range(0, len(_vector1)):
            _chessboardDistanceList.append(Abs(_vector1[i] - _vector2[i]))
        return max2(_chessboardDistanceList)
    elif not len(_vector1) == len(_vector2):
        return vectorEqualityMessage


def BrayCurtisDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        _brayCurtisDistanceNumerator = 0
        _brayCurtisDistanceDenominator = 0
        for i in range(0, len(_vector1)):
            _brayCurtisDistanceNumerator += Abs(_vector1[i] - _vector2[i])
            _brayCurtisDistanceDenominator += Abs(_vector1[i] + _vector2[i])
        return _brayCurtisDistanceNumerator / _brayCurtisDistanceDenominator
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def CanberraDistance(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        _canberraDistance = 0
        for i in range(0, len(_vector1)):
            _canberraDistance += Abs(_vector1[i] - _vector2[i]) / (Abs(_vector1[i]) + Abs(_vector2[i]))
        return _canberraDistance
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def HammingDistance(_vector1, _vector2):
    if len(_vector1) == len(_vector2):
        if StringQ(_vector1) and StringQ(_vector2):
            _hammingDistance = 0
            for i in range(0, len(_vector1)):
                _hammingDistance += boole(not _vector1[i] == _vector2[i])
            return _hammingDistance
        elif ListQ(_vector1) and ListQ(_vector2):
            _hammingDistance = 0
            for i in range(0, len(_vector1)):
                _hammingDistance += boole(not _vector1[i] == _vector2[i])
            return _hammingDistance
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def VectorAngle(_vector1: list, _vector2: list):
    if len(_vector1) == len(_vector2):
        return ArcCos(dotHelp(_vector1, _vector2))
    elif len(_vector1) != len(_vector2):
        return vectorEqualityMessage


def Norm(_list: list):
    _norm = 0
    for i in _list:
        _norm += i ** 2
    return Sqrt(_norm)


def Normalize(_list: list):
    _normalize = []
    _norm = Norm(_list)
    for i in _list:
        _normalize.append(i / _norm)
    return _normalize


def Unitize(_list: list):
    _unitize = []
    _total = Total(_list)
    for i in _list:
        _unitize.append(i / _total)
    return _unitize


def Differences(*args):
    if len(args) == 1 and ListQ(args[0]):
        _differences = []
        for i in range(1, len(args[0])):
            _differences.append(args[0][i] - args[0][i - 1])
        return _differences
    elif len(args) == 2 and ListQ(args[0]) and NumberQ(args[1]):
        _differences = []
        for i in range(1, len(args[0])):
            _differences.append(args[0][i] - args[1] * args[0][i - 1])
        return _differences
    elif len(args) == 3 and ListQ(args[0]) and NumberQ(args[1]) and IntegerQ(args[2]):
        pass
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        pass


def ListCompare(_list1: list, _list2: list):
    _minLength = min(len(_list1), len(_list2))
    _truthList = []
    for i in range(0, _minLength):
        _truthList.append(_list1[i] == _list2[i])
    return _truthList


def Intersection(*args):
    _intersection = []
    for i in args[0][0]:
        if containedInAllQ(i, args[0]):
            _intersection.append(i)
        else:
            _intersection = _intersection
    return Union(_intersection)


def Complement(_list: list, *args):
    _complement = []
    for i in _list:
        _presence = False
        for _sublist in args:
            _presence = _presence or MemberQ(_sublist, i)
        if not _presence:
            _complement.append(i)
    return _complement


def _pivot(_list: list):
    _pivotPosition = randrange(0, len(_list))
    _skippedRange = list(range(0, len(_list)))
    _skippedRange.pop(_pivotPosition)

    _pivotValue = _list[_pivotPosition]
    _pivotList = [_pivotValue]
    _prePivotList = []
    _postPivotList = []

    for _i in _skippedRange:
        if _list[_i] < _pivotValue:
            _prePivotList.append(_list[_i])
        elif _list[_i] > _pivotValue:
            _postPivotList.append(_list[_i])
        elif _list[_i] == _pivotValue:
            _pivotList.append(_list[_i])

    return [_postPivotList] + _pivotList + [_prePivotList]


def QuickSort(_list: list):
    _list = [_list]
    while someListQ(_list):
        for i in range(0, len(_list)):
            if ListQ(_list[i]):
                __pivot = _pivot(_list[i])
                _list.pop(i)
                for r in __pivot:
                    if not ListQ(r) or len(r) != 0:
                        _list.insert(i, r)
    return _list


def QuickSortTrack(_list: list, fileName: str):
    TimeTagMessage("Opening file")
    __quickSortExport = open(fileName, 'w')
    _list = [_list]

    TimeTagMessage("Sorting the input list")
    TimeTagMessage("Writing the tracking list to the file")
    while someListQ(_list):
        for i in range(0, len(_list)):
            if ListQ(_list[i]):
                __pivot = _pivot(_list[i])
                _list.pop(i)
                for r in __pivot:
                    if not ListQ(r) or len(r) != 0:
                        _list.insert(i, r)
        __quickSortExport.write("%s\n" % _list)

    TimeTagMessage("Closing the file and wrapping up")
    __quickSortExport.close()
    TimeTagMessage("Export complete ;)")


def QuickSortTrackSteps(_list: list, fileName: str, steps: int):
    TimeTagMessage("Opening file")
    __quickSortExport = open(fileName, 'w')

    TimeTagMessage("Running " + str(steps) + " loops and writing to text file")
    for _track in range(0, steps):
        __track = 1
        _list = [_list]
        while someListQ(_list):
            for i in range(0, len(_list)):
                if ListQ(_list[i]):
                    __pivot = _pivot(_list[i])
                    _list.pop(i)
                    for r in __pivot:
                        if not ListQ(r) or len(r) != 0:
                            _list.insert(i, r)
            __track += 1
        __quickSortExport.write("%s\n" % __track)

        if _track % 1000 == 0:
            TimeTagMessage("Writing the " + str(_track) + "th item to the file")

    TimeTagMessage("Closing the file and wrapping up")
    __quickSortExport.close()
    TimeTagMessage("Export complete ;)")
