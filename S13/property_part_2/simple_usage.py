class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def set_area(self, value):
        ratio = (value / self.get_area())**0.5
        self.a = self.a * ratio

    area = property(get_area, set_area)


class NewSquare:
    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @area.setter
    def area(self, value):
        ratio = (value / self.area)**0.5
        self.a = self.a * ratio











if __name__ == '__main__':
    s = Square(10)
    print(s.a, s.area)
    s.a = 100
    print(s.a, s.area)
    s.area = 1
    print(s.a, s.area)
    del s.a
    print(s.a, s.area)

