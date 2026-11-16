from abc import ABC, abstractmethod

# Abstraction
class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass


# Encapsulation
class SBI(Bank):

    def __init__(self, balance):
        self.__balance = balance

    def interest(self):
        print("Interest rate: 7%")

    def display(self):
        print("Balance:", self.__balance)


obj = SBI(50000)

obj.interest()
obj.display()
