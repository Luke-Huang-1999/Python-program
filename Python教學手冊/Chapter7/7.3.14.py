class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, W, H):
        self.width = W
        self.height = H

    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, R):
        self.radius = R

    def area(self):
        return self.radius**2 * 3.14


rect = Rectangle(4, 5)
circle = Circle(3)
print(rect.area())
print(circle.area())
