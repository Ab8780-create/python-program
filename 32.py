class Student:
    def __init__(self):
        print("Constructor called")

    def display(self):
        print("Student object created")

    def __del__(self):
        print("Destructor called")

s1 = Student()
s1.display()

del s1
