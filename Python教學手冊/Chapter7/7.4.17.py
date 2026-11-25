class Student:
    def __init__(self, N, A):
        self.__name = N
        self.__age = A

    def set_name(self, new_N):
        self.__name = new_N

    def set_age(self, new_A):
        if self.validate_age(new_A):
            self.__age = new_A
    def get_info(self):
        return f"{self.__name}, {self.__age} years old"
    def validate_age(self, new_A):
        if 18 <= new_A <= 25:
            return True
        else:
            print("無效的年齡")
            return False


student = Student("Alice", 20)
print(student.get_info())
student.set_age(150)