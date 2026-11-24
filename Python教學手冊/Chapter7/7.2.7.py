class Employee:
    company = "Unknown"
    def __init__(self, Name, Salary):
        self.name = Name
        self.salary = Salary
    def display_info(self):
        return f"姓名：{self.name}，薪水：{self.salary}，公司：{Employee.company}"

Employee.company = "TechCorp"
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
print(emp1.display_info())
print(emp2.display_info())