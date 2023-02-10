from sys import stdout
import sys
from functions.lists import equal_all, range2
from functions.random_functions import RandomChoice

_folderPath = 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_10_exercise_3.022\\'
for _n in [10, 15]:
    _steps = 10000
    _subSteps = _steps // 100
    __n = _n
    _set = range2(_n)

    for _k in range(2, 5):
        _progressPad = "_" * 106
        _file = open(
            _folderPath + 'sheldon_ross_10_exercise_3.022_' + str(_n) + '_' + str(
                _k) + '.txt', 'w')

        print("\n\nWriting data to the file :" + _file.name)
        print(_progressPad)

        for i in range(0, _steps):
            _sample = RandomChoice(_set, _k)
            while True:
                if equal_all(_sample[-_k:]):
                    break
                else:
                    _sample.append(RandomChoice(_set))
            _file.write(_sample.__str__().replace("[", "{").replace("]", "}") + '\n')
            if (i + 1) % _subSteps == 0:
                stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(
                    i // _subSteps + 1) + " %")
                stdout.flush()
    print("\nClosing the file: " + _file.name)
    _file.close()
