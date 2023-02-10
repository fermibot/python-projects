from sys import stdout
from functions.lists import range2
import csv
from functions.sheldon_ross_support_functions import randomChoiceCustom

_folderPath = 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_10_exercise_3.029\\'

_csvfile = open(_folderPath + 'sheldon_ross_10_exercise_3.029.csv', 'w', newline='')
_csvWriter = csv.writer(_csvfile)

_steps = 10000
_subSteps = _steps // 100
_progressPadTop = "-" * 106
_progressPadBottom = "-" * 106
_masterList = []

print("\n\nWriting data to the file :" + _csvfile.name)
print(_progressPadTop)

for i in range(0, _steps):
    __games = []
    for _pA in range2(0.05, 1.00, 0.05):
        _probabilities = [_pA, 1 - _pA]
        __i = 0
        __game = []
        while True:
            __game.append(randomChoiceCustom(_probabilities[__i % 2]))
            __i += 1
            if __game[-2:] == [1, 1]:
                break
        __games.append(__game.__len__())
    _csvWriter.writerow(__games)

    if (i + 1) % _subSteps == 0:
        stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(i // _subSteps + 1) + " %")
        stdout.flush()

print("\n" + _progressPadBottom)
print("Closing the file: " + _csvfile.name)

_csvfile.close()
