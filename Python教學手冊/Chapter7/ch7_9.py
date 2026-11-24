class Phone:
    def __init__(self, brand):
        self.brand = brand

class Smartphone(Phone):
    def __init__(self, brand, os):
        super().__init__(brand)
        self.os = os
    def info(self):
        print(f"{self.brand}智慧型手機，操作系統{self.os}")

my_phone = Smartphone("Apple", "ios")
my_phone.info()

# super() 的作用是：
# 呼叫父類別（Parent Class）的方法，
# 讓子類別（Child Class）可以沿用父類別已經定義好的功能。