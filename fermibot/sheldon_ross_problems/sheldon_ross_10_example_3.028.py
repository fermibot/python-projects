from functions.random_functions import *
from functions.lists import *
from functions.monitoring import *
from fermibot.sheldon_ross_problems.sheldon_ross_utilities import *
import csv

unknownPath = open('folderPath.txt').readlines()[0]
chapterName = 'sheldon_ross_chapter_03'
problemName = 'sheldon_ross_10_example_3.028'


_x = range2(1, 100)
for __x in _x:
    __xList = []
    __fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName], '_1_through_100_' + str(__x) +
                                   '.csv')
    TimeTagMessage('Opening file ' + __fileName)
    __file = open(__fileName, 'w')
    TimeTagMessage('Opening writer object')
    __writer = writer = csv.writer(__file, delimiter=',')
    for i in range(1000000):
        _randomSum = RandomReal()
        _randomSumCount = 1
        _randomElement = RandomReal()
        while _randomSum < __x:
            _randomSum += RandomReal()
            _randomSumCount += 1
        __xList.append(_randomSumCount)
    TimeTagMessage('Writing row ' + str(__x) + ' the file')
    writer.writerow(__xList)
    TimeTagMessage('Closing the file ' + __fileName)
    __file.close()

