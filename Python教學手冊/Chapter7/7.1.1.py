class Window():
    def __init__(self, W = 10, H = 5):
        self.width = W
        self.heigth = H
    def area(self):
        return self.width * self.heigth
w0 = Window()
w1 = Window(12,8)

print(w0.area())
print(w1.area())