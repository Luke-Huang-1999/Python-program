class Student:
    student_count = 0

    @classmethod
    def get_student_count(cls):
        return Student.student_count

    def __init__(self, N):
        self.name = N
        Student.student_count += 1


s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")
print(Student.get_student_count())
