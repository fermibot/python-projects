from functions.random_functions import *
from functions.lists import *
from functions.monitoring import *
from fermibot.sheldon_ross_problems.sheldon_ross_utilities import *

unknownPath = open('folderPath.txt').readlines()[0]
chapterName = 'sheldon_ross_chapter_03'
problemName = 'sheldon_ross_10_example_3.025'


def bestGift():
    for variableGifts in [10, 50, 100]:
        numberOfGifts = variableGifts

        for rejInd in range(0, numberOfGifts):
            __fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName],
                                           '_' + str(numberOfGifts) + '_'
                                           + str(rejInd) + '.txt')
            __file = open(__fileName, 'w')

            TimeTagMessage('Opening file ' + __fileName)
            TimeTagMessage('Writing into file')

            for r in range(1, 1000000):
                randomSample = RandomSample(range2(numberOfGifts), numberOfGifts)
                rejectedIndex = rejInd
                rejectedSequence = randomSample[0:rejectedIndex]
                unRejectedSequence = randomSample[rejectedIndex:len(randomSample)]

                accepted = None
                for i in unRejectedSequence:
                    if greater_than_all(i, rejectedSequence):
                        accepted = i
                        break
                __file.write(str(accepted) + '\n')

            TimeTagMessage('Closing the file ' + __fileName)
            __file.close()
            print('')


def worstGift():
    for variableGifts in [10, 50, 100]:
        numberOfGifts = variableGifts

        for rejInd in range(0, numberOfGifts):
            __fileName = ConstructFileName([unknownPath, chapterName, problemName, problemName],
                                           '_worst_' + str(numberOfGifts) + '_'
                                           + str(rejInd) + '.txt')
            __file = open(__fileName, 'w')

            TimeTagMessage('Opening file ' + __fileName)
            TimeTagMessage('Writing into file')

            for r in range(1, 1000000):
                randomSample = RandomSample(range2(numberOfGifts), numberOfGifts)
                rejectedIndex = rejInd
                rejectedSequence = randomSample[0:rejectedIndex]
                unRejectedSequence = randomSample[rejectedIndex:len(randomSample)]

                accepted = None
                for i in unRejectedSequence:
                    if less_than_all(i, rejectedSequence):
                        accepted = i
                        break
                __file.write(str(accepted) + '\n')

            TimeTagMessage('Closing the file ' + __fileName)
            __file.close()
            print('')


if __name__ == '__main__':
    bestGift()
    worstGift()
