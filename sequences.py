from typing import List
from collections.abc import Iterable


class ArithmeticSequences:

    def __init__(self, a1: float, d1: float):
        self.a = a1
        self.d = d1

    def arithmetic_number(self, n: int) -> float:
        return self.a + (n - 1) * self.d

    def arithmetic_sequence(self, n: int) -> Iterable:
        for i in range(1, n + 1):
            yield self.arithmetic_number(i)

    @staticmethod
    def arithmetic_detect(a_1: float, a_2: float, a_3: float) -> List[float] or None:
        if a_3 - a_2 != a_2 - a_1:
            print("The sequence entered is not arithmetic")
            return None
        else:
            return [a_1, a_2 - a_1]


if __name__ == '__main__':
    myClass = ArithmeticSequences(1, 1)
    for number in myClass.arithmetic_sequence(100):
        print(number)
    print(myClass.arithmetic_detect(1, 1, 2))
