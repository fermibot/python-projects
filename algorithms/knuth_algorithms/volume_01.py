from typing import List
from functions.mathematical_functions import LogE


def vol_01_chapter_01_algorithm_e(m: int, n: int, print_q: bool = False) -> int:
    """Algorithm E: Euler's method of finding GCD"""
    while m % n > 0:
        m, n = n, m % n
        if print_q:
            print(m, n, m % n)
    return n


def vol_01_exercise_01_01_001(a, b, c, d):
    """exchanging 4 variables"""
    r, b, c, d = b, c, d, a
    a = r
    return a, b, c, d


def vol_01_exercise_01_01_002(m: int, n: int) -> int:
    """Algorithm F, a modified version of algorithm E"""
    # TODO: Revisit this one
    return 0


def vol_01_exercise_01_01_006_pre(n: int, m: int) -> int:
    r = 0
    while m % n > 0:
        r += 1
        m, n = n, m % n
    return r


def vol_01_exercise_01_01_006(r_in: int = 100) -> List[int]:
    count_list = []
    for r in range(1, r_in + 1):
        count_list.append(vol_01_exercise_01_01_006_pre(r, 5))
    return count_list


def vol_01_exercise_01_01_010(x) -> float:
    return LogE(x)


if __name__ == '__main__':
    print(2 * vol_01_exercise_01_01_010(10))
