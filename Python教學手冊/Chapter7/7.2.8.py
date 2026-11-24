class Temperture:
    def __init__(self, F):
        self.fahrenheit = F

    @classmethod
    def from_celsius(cls, C):
        return cls(C * 9/5 + 32)

temp = Temperture.from_celsius(25)
print(temp.fahrenheit)