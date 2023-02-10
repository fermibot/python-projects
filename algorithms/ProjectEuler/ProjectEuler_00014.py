import sys



def CollatzSequence(_integer: int) -> int:
    integer = _integer
    length = 1
    while True:
        if integer == 1:
            break
        else:
            if integer % 2 == 0:
                integer = integer // 2
            elif integer % 2 == 1:
                integer = 3 * integer + 1
        length += 1
    return length


if __name__ == '__main__':
    collatzList = []
    for i in range(1, 1000001):
        sys.stdout.write(f"\rCurrently processing integer::{i}")
        collatzList.append(CollatzSequence(i))

    maxCollatz = max(collatzList)
    print(f"\n{[collatzList.index(maxCollatz) + 1, maxCollatz]}")
