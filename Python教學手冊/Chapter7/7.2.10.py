class Circle:
    # radius = 0
    # def __inti__(self, R):
    #     self.radius = R
    @staticmethod
    def area(radius):
        return radius**2 * 3.14

    @staticmethod
    def perimeter(radius):
        return radius * 2 * 3.14

radius = 5
print(f"{Circle.area(radius):.2f}")
print(f"{Circle.perimeter(radius):.2f}")