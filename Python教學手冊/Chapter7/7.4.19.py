class Rectangle:
    def __init__(self, W, H):
        self.__width = W
        self.__height = H

    @property
    def area(self):
        return self.__height * self.__width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_W):
        if new_W >= 0:
            self.__width = new_W
        else:
            print("寬度不能為負數，設置為 0")
            self.__width = 0

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_H):
        if new_H >= 0:
            self.__height = new_H
        else:
            print("高度不能為負數，設置為 0")
            self.__height = 0

rect = Rectangle(5,10)
print(rect.area)
rect.width = -3
rect.height = -2
print(rect.area)