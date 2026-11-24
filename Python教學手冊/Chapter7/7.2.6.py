class Circle:
    pi = 3.14159

    def __init__(self, R):
        self.rad = R

    def area(self):
        print(f"面積：{self.rad ** 2 * Circle.pi:.2f}")

    def perimeter(self):
        print(f"周長：{self.rad * 2 * Circle.pi:.2f}")


c1 = Circle(5)
c1.area()
c1.perimeter()

Circle.pi = 3.14
c2 = Circle(5)
c2.area()
c2.perimeter()
