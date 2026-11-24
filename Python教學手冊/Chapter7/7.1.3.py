class Calculator:
    def __init__(self, a, b):
        self.n1 = a
        self.n2 = b

    def add(self):
        return self.n1 + self.n2

    def gcd(self):
        num1 = self.n1
        num2 = self.n2
        Small_num = num1 if num1 <= num2 else num2
        for i in range(min(num1, num2), 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                break
        return i

    def lcm(self):
        num1 = self.n1
        num2 = self.n2
        for i in range(max(num1, num2), num1 * num2 + 1):
            if i % num1 == 0 and i % num2 == 0:
                break
        return i

    def power(self):
        return self.n1**self.n2


c0 = Calculator(2, 10)
print(c0.add())
print(c0.gcd())
print(c0.lcm())
print(c0.power())
