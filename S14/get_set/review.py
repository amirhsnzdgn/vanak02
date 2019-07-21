class Area:
    def __get__(self, instance, owner):
        return instance.a ** 2

    def __set__(self, instance, value):
        ratio = (value / instance.area) ** 0.5
        instance.a = instance.a * ratio


class Square:
    area = Area()

    def __init__(self, a):
        self.a = a


s = Square(10)
print(s.a, s.area)
s.area = 25
print(s.a, s.area)