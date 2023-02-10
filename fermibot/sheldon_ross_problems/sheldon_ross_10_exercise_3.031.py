from sys import stdout
import csv
from functions.sheldon_ross_support_functions import randomChoiceCustom

_folderPath = 'D:\\Mathematica Files 4K\\sheldon_ross\\sheldon_ross_chapter_03\\sheldon_ross_10_exercise_3.031\\'

for _p in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]:

    _csvfile = open(_folderPath + 'sheldon_ross_10_exercise_3.031_' + _p.__str__() + '.csv', 'w', newline='')
    _csvWriter = csv.writer(_csvfile)

    _steps = 10000
    _subSteps = _steps // 100
    _progressPadTop = "-" * 106
    _progressPadBottom = "-" * 106
    _masterList = []

    print("\n\nWriting data to the file :" + _csvfile.name)
    print(_progressPadTop)

    _masterSequenceFlips = []
    for i in range(0, _steps):
        __games = []

        _bitSequence = []
        _tracker = 0
        while True:
            _bitSequence.append(randomChoiceCustom(_p))
            if _bitSequence.__len__() > 1 and _bitSequence[-1] != _bitSequence[-2]:
                _tracker += 1
            if _tracker == 2:
                del _bitSequence[-1]
                _csvWriter.writerow(_bitSequence)
                break

        if (i + 1) % _subSteps == 0:
            stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(i // _subSteps + 1) + " %")
            stdout.flush()

    print("\n" + _progressPadBottom)
    print("Closing the file: " + _csvfile.name)
    _csvfile.close()