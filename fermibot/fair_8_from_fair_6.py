import random
import math


def binaryFromSix():
    return math.ceil(random.randint(1, 6) / 3)


fairEight = {
    1: {1: {1: 1, 2: 2}, 2: {1: 3, 2: 4}},
    2: {1: {1: 5, 2: 6}, 2: {1: 7, 2: 8}}
}

if __name__ == '__main__':
    for i in range(100):
        print(fairEight[binaryFromSix()][binaryFromSix()][binaryFromSix()], end=' ')
