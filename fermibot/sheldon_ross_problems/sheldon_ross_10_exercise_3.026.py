from sys import stdout
from functions.lists import range2
import csv
from functions.sheldon_ross_support_functions import randomChoiceCustom

_folderPath = 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_10_exercise_3.026\\'


_csvfile = open(_folderPath + 'sheldon_ross_10_exercise_3.26.csv', 'w', newline='')
_csvWriter = csv.writer(_csvfile)

_steps = 1000
_subSteps = _steps // 100
_progressPadTop = "-" * 106
_progressPadBottom = "-" * 106
_masterList = []

print("\n\nWriting data to the file :" + _csvfile.name)
print(_progressPadTop)

for i in range(0, _steps):
    _gamesMaster = []
    for _pB in range2(0.1, 0.9, 0.1):
        for _pA in range2(0.1, 0.9, 0.1):
            __i = 0
            _games = []
            _probabilities = [_pA, _pB]
            while True:
                _games.append(randomChoiceCustom(_probabilities[__i % 2]))
                __i += 1
                if _games[-2:] == [1, 1]:
                    break
            _gamesMaster.append(_games.__len__())
    _csvWriter.writerow(_gamesMaster)

    if (i + 1) % _subSteps == 0:
        stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(i // _subSteps + 1) + " %")
        stdout.flush()

print("\n" + _progressPadBottom)
print("Closing the file: " + _csvfile.name)

_csvfile.close()
