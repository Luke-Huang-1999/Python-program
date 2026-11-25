class Animal:
    def make_sound(self):
        print("動物發出聲音")

class Dog(Animal):
    def make_sound(self):
        print("汪汪")

dog = Dog()
dog.make_sound()