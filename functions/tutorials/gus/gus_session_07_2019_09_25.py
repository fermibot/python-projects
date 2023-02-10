from typing import List


def triangular_detect(coord: List[List[float]]) -> bool:
    pre_truth = True

    for i in coord:
        for j in i:
            pre_truth = (pre_truth and ((type(j) == float) or (type(j) == int)))

    if not pre_truth:
        return False

    elif pre_truth:
        equality_truth = False
        for i in range(len(coord)):
            for j in range(i + 1, len(coord)):
                equality_truth = equality_truth or (coord[i] == coord[j])
        if equality_truth:
            return False
        else:
            slope = coord[1][1] - coord[0][1] / coord[1][0] - coord[0][0]
            y_intercept = coord[1][1] - slope * coord[1][0]
            print([slope, y_intercept])
            if coord[2][1] == slope * coord[2][0] + y_intercept:
                return False
            else:
                return True


if __name__ == '__main__':
    print(triangular_detect([[0, 0], [1, 1], [1.5, 3]]))
