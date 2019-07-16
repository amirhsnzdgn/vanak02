class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, Square):
            return instance.a ** 2
        if isinstance(instance, Circle):
            return 3.1415 * instance.r ** 2

    def __set__(self, instance, value):
        ratio = (value / instance.area) ** 0.5
        if isinstance(instance, Square):
            instance.a *= ratio
        if isinstance(instance, Circle):
            instance.r *= ratio


class Square:
    area = Area()

    def __init__(self, a):
        self.a = a


class Circle:
    area = Area()

    def __init__(self, r):
        self.r = r


if __name__ == '__main__':
    s = Circle(10)
    print(s.r, s.area)
    s.area = 1
    print(s.r, s.area)
    s.a = 100
    print(s.r, s.area)
