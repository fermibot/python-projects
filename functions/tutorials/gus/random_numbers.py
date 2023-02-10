from random import uniform, _pi

random_sum = 0


def area_of_crescent() -> None:
    for max_darts in range(1, 6):
        number_of_darts = 10 ** max_darts
        between_square_and_circle = 0
        area_of_square = 16
        for i in range(0, number_of_darts):
            x_coordinate = uniform(a=-2, b=2)
            y_coordinate = uniform(a=-2, b=2)
            if x_coordinate ** 2 + y_coordinate ** 2 >= 4 and -2 <= x_coordinate <= 2 and -2 <= y_coordinate <= 2:
                between_square_and_circle += 1
            area_of_object = area_of_square * between_square_and_circle / number_of_darts
        print(f"NumberOfDarts::{number_of_darts}||EstimatedArea::{area_of_object}")


def area_between_circle_and_ellipse() -> None:
    for max_darts in range(1, 6):
        minor_axis = 1
        major_axis = 2
        area_of_ellipse = _pi * major_axis * minor_axis
        n_darts = 10 ** max_darts
        number_of_hits = 0
        number_of_misses = 0
        for i in range(0, n_darts):
            x_coord = uniform(a=-2, b=2)
            y_coord = uniform(a=-1, b=1)
            if (x_coord ** 2 + y_coord ** 2 > 1) and (x_coord / 2) ** 2 + (y_coord / 1) ** 2 < 1:
                number_of_hits += 1
            else:
                number_of_misses += 1
            area_obj = area_of_ellipse * number_of_hits / n_darts
            area_of_non = 8 * number_of_misses / n_darts
        yield f"NumberOfDarts::{n_darts}||EstimatedArea::{area_obj}"


def hit_check(x_loc: float, y_loc: float, radius: float, x_rand: float, y_rand: float) -> bool:
    if ((x_rand - x_loc) ** 2) + ((y_rand - y_loc) ** 2) > radius ** 2:
        return True
    else:
        return False


def area_between_multiple_circles(n_darts: int) -> float:
    n_darts_internal = n_darts
    n_hits = 0
    n_misses = 0
    for i in range(0, n_darts_internal):
        x_coord = uniform(a=-2, b=2)
        y_coord = uniform(a=-1.5, b=1)

        if hit_check(-1, 0, 1, x_coord, y_coord) and hit_check(0.5, -0.5, 1.5, x_coord, y_coord):
            n_hits += 1
        else:
            n_misses += 1

        proportion_of_area_outside_both = n_hits / n_darts_internal
        area_of_rectangle = 2.5 * 4.0
    return proportion_of_area_outside_both * area_of_rectangle


if __name__ == '__main__':
    for j in range(0, 10):
        for power in range(0, 5):
            print(f"Number of Darts = {10**power}||Calculated Area = {area_between_multiple_circles(10 ** power)}")
        print()
