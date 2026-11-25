class Car:

    def __init__(self, C):
        self.color = C
    # @staticmethod
    def show():
        print(f"color = {Car.color}")

class Truck(Car):
    def __init__(self, Door, Owner, Color):
        super().__init__(Color)
        self.door = Door
        self.owner = Owner
        # self.color = Color
    def show(self):
        print(f"doors = {self.door}, owner = {self.owner}, color = {self.color}")

truck = Truck(4, "Alice", "Red")
truck.show()