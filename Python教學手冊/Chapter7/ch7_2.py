class Circle:
    def __init__(self, rad = 1):#初始化函數
        self.radius = rad  
    def area(self):
        return 3.14*self.radius ** 2
    def perimeter(self):
        return 2 * 3.14*self.radius

c1 = Circle(4)
c2 = Circle()
print(f"半徑：{c1.radius}，面積：{c1.area()}, 周長：{c1.perimeter()}")
print(f"半徑：{c2.radius}，面積：{c2.area()}, 周長：{c2.perimeter()}")

