from typing import List


def demonstration(integer: int = 10) -> List[int]:
    list_out = []
    for i in range(0, integer + 1):
        list_out.append(i)
    return list_out


def yield_demonstration(integer: int = 10) -> int:
    for i in range(0, integer + 1):
        yield i


if __name__ == '__main__':

    for i in demonstration(10):
        print(i)

    for i in yield_demonstration(10):
        print(i)
