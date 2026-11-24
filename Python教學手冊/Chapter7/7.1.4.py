class Person:
    def __init__(self, N, A):
        self.name = N
        self.age = A
    def greet(self):
        print(f"嗨，我是{self.name}，{self.age}歲")

p = Person("Alice", 21)
p.greet()