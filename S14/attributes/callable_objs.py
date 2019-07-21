# a()          #  __call__
# a[]          #  __getitem__ __setitem__
# a.whatever   #  __getattr__


def multiply(n):
    def inner(s):
        return s * n
    return inner


class Multiply:
    def __init__(self, n: int):
        self.n = n

    def __call__(self, s):
        return s * self.n


f1 = multiply(10)
f2 = Multiply(2)

res1 = f1("a")  # "a" * 10    "aaaaaaaaaa"
res2 = f1(10)  # 100
