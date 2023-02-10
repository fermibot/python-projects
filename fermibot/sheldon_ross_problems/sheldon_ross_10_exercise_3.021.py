from sys import stdout
from functions.random_functions import RandomChoice, RandomReal

print("Opening the text file")
_file = open(
    'D:\Mathematica Files 4K\sheldon_ross\sheldon_ross_chapter_03\sheldon_ross_10_exercise_3.021\sheldon_ross_10_exercise_3.021.txt',
    'w')

print("Initializing the loop and writing to the text file")

print("_" * 106)

_steps = 10000000
_subSteps = _steps // 100
for i in range(0, _steps):
    _n, _time = 0, 0
    while True:
        _n += 1
        _rand = RandomReal()
        if 0 <= _rand < 1 / 3:
            _time += 2
            break
        elif 1 / 3 <= _rand < 2 / 3:
            _time += 3
        elif 2 / 3 <= _rand <= 1:
            _time += 5
    _file.write({_n, _time}.__str__() + '\n')
    if (i + 1) % _subSteps == 0:
        stdout.write("\r" + ("\r" + ("#" * (i // _subSteps + 1)).ljust(100)) + " " + str(i // _subSteps + 1) + " %")
        stdout.flush()
