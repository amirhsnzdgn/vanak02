class Color:
    color_map = {'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'cyan': 6, 'purple': 5, 'gray': 7}
    font_map = {'regular': 0, 'bold': 1, 'underlined': 4}

    def __init__(self, color, style=3, font='regular'):
        self.color = self.color_map[color]
        self.style = style
        self.font = self.font_map[font]

    def __call__(self, fn):
        def inner(x):
            out = f"\033[{self.style}{self.color};{self.font}m{fn(x)}\033[0m"
            return out

        return inner


@Color('green', style=3)
def echo1(s):
    return s


@Color('green', style=4, font='bold')
def echo2(s):
    return s


@Color('green', style=9, font='underlined')
def echo3(s):
    return s


print(echo1("hello"))
print(echo2("hello"))
print(echo3("hello"))
