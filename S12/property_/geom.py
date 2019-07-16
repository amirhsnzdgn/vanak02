class Rectangle:
    """

    Example
    -------
    >>> rect = Rectangle(10.0, 4.0)
    >>> rect.area
    40.0
    >>> rect.area = 160.0
    >>> rect.width
    20.0
    >>> rect.height
    8.0
    """
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = (value / self.area) ** 0.5
        self.width *= ratio
        self.height = self.height * ratio

    @property
    def perimeter(self) -> float:
        return (self.width + self.height) * 2

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.area
        self.width *= ratio
        self.height = self.height * ratio



if __name__ == '__main__':
    import doctest

    doctest.testmod()
