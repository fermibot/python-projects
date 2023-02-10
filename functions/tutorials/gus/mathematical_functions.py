from math import log10, floor


def tribonacci(n: int):
    seed_list = [0, 1, 1]
    if n <= 3:
        return seed_list[n - 1]
    if n > 3:
        for i in range(n - 3):
            new_tribonacci = sum(seed_list[-3:])
            seed_list.append(new_tribonacci)
            seed_list = seed_list[-3:]
        return seed_list[-1]


def fibonacci(n: int):
    seed_list = [1, 1]
    if n <= 2:
        return seed_list[n - 1]
    if n > 2:
        for i in range(n - 2):
            new_tribonacci = sum(seed_list[-2:])
            seed_list.append(new_tribonacci)
            seed_list = seed_list[-2:]
        return seed_list[-1]


def figurate_number(sides: int, n: int):
    offset = sides - 2
    figurate_number_internal = 0
    for i in range(0, n):
        figurate_number_internal += 1 + (offset * i)
    return figurate_number_internal


def integer_digits(integer: int):
    return len(str(integer))


def square_root(number, precision: int = 10):
    square_root_internal = number
    base = floor(log10(number)) - 1
    while base >= -precision:
        base_addition = 10 ** base
        while (square_root_internal - base_addition) ** 2 > number:
            square_root_internal -= base_addition
        base -= 1
    return square_root_internal


if __name__ == '__main__':
    print(square_root(456, precision=14))
