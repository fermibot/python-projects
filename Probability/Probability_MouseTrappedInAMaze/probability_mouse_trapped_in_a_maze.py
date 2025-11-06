import random

import tqdm


def choice_01():
    return random.choices([1, 2], weights=[0.5, 0.5])[0]


def choice_02():
    return random.choices([3, 4], weights=[1 / 3, 2 / 3])[0]


class Maze:
    def __init__(self):
        self.travel_time = []
        self.choices = []

    def solve(self):
        choice_01_door = choice_01()
        self.choices.append(choice_01_door)
        if choice_01_door == 1:
            self.travel_time.append(3)
            return self.solve() + 3
        else:
            choice_02_door = choice_02()
            self.choices.append(choice_02_door)
            if choice_02_door == 3:
                self.travel_time.append(2)
                return 2
            elif choice_02_door == 4:
                self.travel_time.append(5)
                return self.solve() + 5


# (*1=Left; 2=Right; 3: Second right: 2; Second left: ;*)
# Choice1 := RandomChoice[{0.5, 0.5} -> {1, 2}]
# Choice2 := RandomChoice[{1/3, 2/3} -> {3, 4}]
#
# Maze := Module[{door1 = Choice1, door2 = Choice2},
#   If[door1 == 2, Maze + 3,
#    If[door2 == 3, 2, If[door2 == 4, Maze + 5]]
#    ]
#   ]


if __name__ == '__main__':
    journeys = [100]
    for i in tqdm.tqdm(range(1000)):
        maze = Maze()
        journey = maze.solve()
        journeys.append(maze)
