from functions.random_functions import RandomChoice, RandomInteger

_masterList = []
for r in range(0, 1000000):
    _list = []
    _i = 1

    while True:
        if _i == 5:
            _list.append(5)
        elif _i < 6 and _i != 5:
            _rand = RandomChoice([1, 2, 3, 4, 6])
            _list.append(_rand)
        elif _i >= 6:
            _rand = RandomInteger(1, 6)
            if _rand != 6:
                _list.append(_rand)
            elif _rand == 6:
                _list.append(_rand)
                break
        _i = _i + 1
    _masterList.append(_list.index(6) + 1)

_file = open('D:\Mathematica Files 4K\sheldon_ross\sheldon_ross_chapter_03\sheldon_ross_10_exercise_3.008\sheldon_ross_10_exercise_3.008.txt', 'w')
for r in _masterList:
    _file.write(r.__str__() + '\n')
