import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Element:
    def __init__(self, s: Node, e: Node):
        self.start = s
        self.end = e

    @property
    def length(self):
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y
        return np.sqrt(dx ** 2 + dy ** 2)

    def show(self):
        plt.plot([self.start.x, self.end.x], [self.start.y, self.end.y], 'bo--')


class Truss:
    def __init__(self, *elements):
        self.elements = elements

    def show(self, outfile=None):
        for el in self.elements:
            el.show()

        if outfile is None:
            plt.show()
        else:
            plt.savefig(outfile)
