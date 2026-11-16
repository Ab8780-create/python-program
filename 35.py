# Single Inheritance
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

obj = Child()
obj.show()
obj.display()


# Multilevel Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()


# Multiple Inheritance
class Father:
    def father(self):
        print("Father class")

class Mother:
    def mother(self):
        print("Mother class")

class Son(Father, Mother):
    def son(self):
        print("Son class")

obj = Son()
obj.father()
obj.mother()
obj.son()
