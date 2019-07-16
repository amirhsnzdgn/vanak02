# from typing import TypeVar
#
#
# T = TypeVar('T')


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    v1 = Vector(1.0, 2.0)
    v2 = Vector(2.0, 2.0)

    v3 = v1 + v2
