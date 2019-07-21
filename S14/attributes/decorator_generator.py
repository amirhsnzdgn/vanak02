def shape(s):
    def decorator(fn):
        def inner(x):
            out = f"{s}{fn(x)}{s}"
            return out

        return inner

    return decorator


class Shape:
    def __init__(self, s):
        self.s = s

    def __call__(self, fn):
        def inner(x):
            out = f"{self.s}{fn(x)}{self.s}"
            return out

        return inner


@Shape("*")
def echo1(s):
    return s


@shape("*")
def echo2(s):
    return s


print(echo("hello"))
