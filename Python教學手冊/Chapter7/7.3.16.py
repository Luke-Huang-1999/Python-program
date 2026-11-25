class Person:
    def __init__(self, N):
        self.name = N
    def print_name():
        print(f"{Person.name}")

class Student(Person):
    def __init__(self, N, G):
        super().__init__(N)
        self.gender = G
    def print_info(self):
        print(f"name = {self.name}, gender = {self.gender}")

student = Student("Bob", "Male")
student.print_info()
    