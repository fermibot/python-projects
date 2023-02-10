from typing import List

from functions.tutorials.gus.distances import euclidean_distance


def RectangleQ(coord: List[List[float]]) -> bool:
    pre_truth = len(coord) == 4

    if pre_truth:
        for element in coord:
            pre_truth = pre_truth and len(element) == 2

    if pre_truth:
        for i in range(0, len(coord) - 1):
            for j in range(i + 1, len(coord)):
                pre_truth = pre_truth and (coord[i] != coord[j])

    if pre_truth:
        farthest_distance = 0
        farthest_index = 0

        for i in range(1, len(coord)):
            current_distance = euclidean_distance(coord_1=coord[0], coord_2=coord[i])
            if current_distance > farthest_distance:
                farthest_distance = current_distance
                farthest_index = i

        all_indices = list(range(0, len(coord)))
        all_indices.pop(farthest_index)
        all_indices.pop(0)

        if euclidean_distance(coord_1=coord[all_indices[0]], coord_2=coord[all_indices[1]]) == farthest_distance:
            list_1 = [
                euclidean_distance(coord[0], coord[all_indices[0]]),
                euclidean_distance(coord[0], coord[all_indices[1]])]

            list_2 = [
                euclidean_distance(coord[farthest_index], coord[all_indices[0]]),
                euclidean_distance(coord[farthest_index], coord[all_indices[1]])
            ]

            if sorted(list_1) == sorted(list_2):
                square_q = True
                for distance in list_1 + list_1:
                    square_q = square_q & (distance == list_1[0])
                if square_q:
                    print("The given coordinates also make square")
                return True
        else:
            return False

    else:
        return pre_truth


if __name__ == '__main__':
    print(RectangleQ([[1, 0], [0, -1], [-1, 0], [0, 1]]))
