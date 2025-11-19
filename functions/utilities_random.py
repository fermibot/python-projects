from random import random


def random_uniform_custom(range_min, range_max, sample_size: int = 10):
    if range_min > range_max:
        range_max, range_min = range_min, range_max
    delta = range_max - range_min
    for _ in range(sample_size):
        yield range_min + delta * random()
