from typing import List


def euclidean_distance(coord_1: List[float], coord_2: List[float]) -> float:
    return pow(pow(coord_1[0] - coord_2[0], 2) + pow(coord_1[1] - coord_2[1], 2), 0.5)
