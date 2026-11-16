class Student:
    college = "Marwadi University"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)

s1 = Student("Rahul", 21)
s2 = Student("Amit", 22)

s1.display()
s2.display()
