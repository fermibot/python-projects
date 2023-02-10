from .lists import *
from .string_operations import *


# Arrays
def CenterArray(*args):
    def _centerArrayAssist(*_args):
        # _args[0] = element; _args[1] = length; _args[2] = padding
        __centerArray = ConstantArray(_args[2], _args[1])
        if EvenQ(_args[1]):
            __centerArray[int(_args[1] // 2) - 1] = _args[0]
        elif OddQ(_args[1]):
            __centerArray[int(_args[1] // 2)] = _args[0]
        return __centerArray
    if len(args) == 2 and not ListQ(args[1]):
        return _centerArrayAssist(args[0], args[1], 0)
    elif len(args) == 2 and ListQ(args[1]):
        _centerArray = ConstantArray(0, Last(args[1]))
        _revArgs = Reverse(args[1])
        for i in range(0, len(args[1]) - 1):
            _centerArray = arrayGenerator(_centerArray, _revArgs[i])
        _arrayIndex = '_centerArray'
        for i in args[1]:
            _arrayIndex += '[' + str(findCenter(i)) + ']'
        _arrayIndex += ' = '
        _arrayIndex += str(args[0])
        exec(_arrayIndex)
        # Need to fix this part of the argument
        return _centerArray
    elif len(args) == 3:
        return _centerArrayAssist(args[0], args[1], args[2])
    elif len(args) == 1:
        return _centerArrayAssist(1, args[0], 0)


def ConstantArray(*args):
    def _constantArrayHelp(_obj, _number):
        __constantArrayHelp = []
        for _i in range(0, Round(_number)):
            __constantArrayHelp.append(_obj)
        return __constantArrayHelp
    if len(args) == 2:
        if NumberQ(args[1]):
            _constantArray = []
            for i in range(0, Round(args[1])):
                _constantArray.append(args[0])
            return _constantArray
        if ListQ(args[1]):
            [_dimensions, _constantArray] = [Reverse(args[1]), _constantArrayHelp(args[0], Last(args[1]))]
            for i in range(1, len(args[1])):
                _constantArray = _constantArrayHelp(_constantArray, _dimensions[i])
            return _constantArray
    elif len(args) != 2:
        pass


def CoordinateBoundsArray(*args):
    if len(args) == 1 and ListQ(args[0]):
        _array = []
        xpos = args[0][0][0]
        while xpos <= Floor(args[0][0][1]):
            _arraylet = []
            ypos = args[0][1][0]
            while ypos <= Floor(args[0][1][1]):
                _arraylet.append([xpos, ypos])
                ypos += 1
            _array.append(_arraylet)
            xpos += 1
        return _array

    elif len(args) == 2:
        if ListQ(args[0]) and NumberQ(args[1]):
            pass
        elif ListQ(args[0]) and ListQ(args[1]):
            pass
    elif len(args) == 3:
        pass
    elif len(args) == 4:
        pass


def SparseArray(*args):
    if ListQ(args[0]) and len(args) == 1:
        _list = args[0]
        _maxx = 0
        _maxy = 0
        for i in _list:
            if i[0][0] > _maxx:
                _maxx = i[0][0]
                if i[0][1] > _maxy:
                    _maxy = i[0][1]
        _dimensions = max2([_maxx, _maxy])

        _listDict = {}
        for i in _list:
            _listDict.update({str(i[0]): i[1]})

        _sparseArray = []
        for i in range(1, _dimensions + 1):
            for j in range(1, _dimensions + 1):
                if str([i, j]) in _listDict:
                    _sparseArray.append([[i, j], _listDict[str([i, j])]])
                elif str([i, j]) not in _listDict:
                    _sparseArray.append([[i, j], 0])
        return Partition(_sparseArray, _dimensions)

    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        if len(args[0]) == len(args[1]):

            # added # for PEP warning elimination _list = args[0]
            _transpose = Transpose(args[0])
            _dimensions = max2([max2(_transpose[0]), max2(_transpose[1])])

            _listDict = {}
            for i in range(0, len(args[0])):
                _listDict.update({str(args[0][i]): args[1][i]})

            _sparseArray = []
            for i in range(1, _dimensions + 1):
                for j in range(1, _dimensions + 1):
                    if str([i, j]) in _listDict:
                        _sparseArray.append([[i, j], _listDict[str([i, j])]])
                    elif str([i, j]) not in _listDict:
                        _sparseArray.append([[i, j], 0])
            return Partition(_sparseArray, _dimensions)
        else:
            print("The two lists need to be of equal lengths")
    else:
        print("No, can't do")


def KroneckerDelta(*args):
    _kroneckerDelta = True
    for i in range(1, len(args)):
        _kroneckerDelta = _kroneckerDelta and (args[i - 1] == args[i])
    if _kroneckerDelta:
        return 1
    else:
        return 0


# Matrices
def IdentityMatrix(_size):
    _identityMatrix = []
    for i in range(0, _size):
        _identityRow = []
        for j in range(0, _size):
            if j == i:
                _identityRow.append(1)
            else:
                _identityRow.append(0)
        _identityMatrix.append(_identityRow)
    return _identityMatrix


def DiagonalMatrix(*args):
    if len(args) == 1 and ListQ(args[0]):
        _diagonal = args[0]
        _dimensions, _diagonalMatrix = [len(_diagonal), []]
        for i in range(0, _dimensions):
            _diagonalMatrixRow = []
            for j in range(0, _dimensions):
                if j == i:
                    _diagonalMatrixRow.append(_diagonal[i])
                elif j != i:
                    _diagonalMatrixRow.append(0)
            _diagonalMatrix.append(_diagonalMatrixRow)
        return _diagonalMatrix
    elif len(args) == 2 and ListQ(args[0]):
        _diagonal = args[0]
        _dimensions, _diagonalMatrix = [len(_diagonal) + args[1], []]
        for i in range(0, _dimensions):
            _diagonalMatrixRow = []
            for j in range(0, _dimensions):
                if j == i + args[1]:
                    _diagonalMatrixRow.append(_diagonal[i])
                elif j != i + args[1]:
                    _diagonalMatrixRow.append(0)
            _diagonalMatrix.append(_diagonalMatrixRow)
        return _diagonalMatrix
    elif len(args) == 3 and ListQ(args[0]):
        _diagonal = args[0] + ConstantArray(0, args[1] + args[2])
        _dimensions, _diagonalMatrix = [len(_diagonal), []]
        for i in range(0, _dimensions):
            _diagonalMatrixRow = []
            for j in range(0, _dimensions):
                if j == i + args[1]:
                    _diagonalMatrixRow.append(_diagonal[i])
                elif j != i + args[1]:
                    _diagonalMatrixRow.append(0)
            _diagonalMatrix.append(_diagonalMatrixRow)
        return _diagonalMatrix


def BoxMatrix(*args):
    _boxMatrix = []
    if len(args) == 1 and not ListQ(args[0]):
        for i in range(-args[0], args[0] + 1):
            _boxRow = []
            for j in range(-args[0], args[0] + 1):
                _boxRow.append(1)
            _boxMatrix.append(_boxRow)
        return _boxMatrix
    elif len(args) == 2:
        _limit = args[0]
        for i in range(-args[1], args[1] + 1):
            _boxRow = []
            for j in range(-args[1], args[1] + 1):
                if (-_limit <= j <= _limit) and (-_limit <= i <= _limit):
                    _boxRow.append(1)
                else:
                    _boxRow.append(0)
            _boxMatrix.append(_boxRow)
        return _boxMatrix
    elif len(args) == 1 and ListQ(args[0]):
        _dimensions = []
        for i in args[0]:
            _dimensions.append(2 * i + 1)
        return ConstantArray(1, _dimensions)


def CrossMatrix(*args):
    if len(args) == 1 and not ListQ(args[0]):
        _crossMatrix = ConstantArray(0, [2 * args[0] + 1, 2 * args[0] + 1])
        _crossMatrix[findCenter(Length(_crossMatrix))] = ConstantArray(1, Length(_crossMatrix))
        for i in range(0, len(_crossMatrix)):
            _crossMatrix[i][args[0]] = 1
        return _crossMatrix
    elif len(args) == 1 and ListQ(args[0]):
        [_dimensions, _indices, _preIndices, arg_len] = [[], [], [], len(args[0])]
        for i in args[0]:
            _preIndices.append([i])
        for i in range(0, arg_len):
            _indices.append(ToString(_preIndices))
            _indices[i][i] = '[j]'
            _indices[i] = "_crossMatrix" + StringJoin(_indices[i]).replace("'", "") + " = 1"
        for i in args[0]:
            _dimensions.append(2 * i + 1)
        _crossMatrix = ConstantArray(0, _dimensions)
        for i in range(0, len(args[0])):
            for j in range(0, _dimensions[i]):
                exec(_indices[i])
        return _crossMatrix
    elif len(args) == 2:
        pass
    elif len(args) == 3:
        pass


def DistanceMatrix(*args):
    def _distanceMatrixHelp(_vector1: list, _vector2: list):
        _distanceMatrix = []
        for i in _vector1:
            _distanceMatrixRow = []
            for j in _vector2:
                _distanceMatrixRow.append(Abs(i - j))
            _distanceMatrix.append(_distanceMatrixRow)
        return _distanceMatrix

    if len(args) == 1 and ListQ(args[0]):
        return _distanceMatrixHelp(args[0], args[0])
    elif len(args) == 2 and ListQ(args[0]) and ListQ(args[1]):
        return _distanceMatrixHelp(args[0], args[1])


def Dot(_array1, _array2):
    if allListQ([_array1, _array2]) and not MatrixQ(_array1) and not MatrixQ(_array2):
        if len(_array1) == len(_array2):
            return dotHelp(_array1, _array2)
        elif len(_array1) != len(_array2):
            return vectorEqualityMessage

    elif MatrixQ(_array1) and MatrixQ(_array2):
        [_array1, _array2] = [_array1, Transpose(_array2)]
        _dot = []
        for i in _array1:
            _dotrow = []
            for j in _array2:
                _dotrow.append(dotHelp(i, j))
            _dot.append(_dotrow)
        return _dot


def Cross(_vectors: list):
    if not MatrixQ(_vectors):
        return "The list is not even all vectors. How do you want me to calculate the cross product? \n" \
               "Die Liste ist nicht einmal alle Vektoren. Wie soll ich das Kreuzprodukt berechnen? \n" \
               "జాబితా అన్ని వెక్టర్స్ కూడా కాదు. క్రాస్ ఉత్పత్తిని నేను ఎలా లెక్కించగలను? \n"
    elif MatrixQ(_vectors):
        pass


def Det(_matrix: list):

    def _elementFinder(_list: list):
        _len = len(_list)
        _elementFinderString = ""
        for i in range(0, _len):
            _elementFinderString += "_mat[" + ToString(i) + "][" + ToString(_list[i] - 1) + "] * "
        _elementFinderString = _elementFinderString[:-3]
        return _elementFinderString

    if MatrixQ(_matrix):
        _len = len(_matrix)
        _det = "("
        _indices = Permutations(range2(_len))
        _mat = _matrix

        for i in _indices:
            _det += _elementFinder(i) + ") + ("
        _det = _det[:-3]
        _det = eval(_det)
        return _det

    else:
        return "The list is not even all vectors. How do you want me to calculate the cross product? \n" \
               "Die Liste ist nicht einmal alle Vektoren. Wie soll ich das Kreuzprodukt berechnen? \n" \
               "జాబితా అన్ని వెక్టర్స్ కూడా కాదు. క్రాస్ ఉత్పత్తిని నేను ఎలా లెక్కించగలను? \n"


# EXPERIMENTAL
#
# def _listBuilder(_list: list, _n: int):
#     _listBuilder = []
#     for i in range(0, _n):
#         _listBuilder.append(_list)
#     return _listBuilder
#
#
# _list = Range(5)
# for i in ConstantArray(5, 3):
#     _list = _listBuilder(_list, i)
#
# print(_list)
#
#
# def levelAnalyzer(_list: list):
#     _list = str(_list)
#     _elements = Union(Characters(_list))
#     _filteredElements = []
#     for i in _elements:
#         if i not in ('[', ']'):
#             _filteredElements.append(i)
#     for i in _filteredElements:
#         _list = _list.replace(i, '')
#
#     _count = 0
#     _bracket = '['
#     _countList = []
#     for i in _list:
#         if i == _bracket:
#             _count += 1
#         else:
#             _countList.append(_count)
#             _count = 0
#     return _countList
#
# print(levelAnalyzer(_list))
