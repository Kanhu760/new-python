class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no #Public attributes.
        self.__acc_pass = acc_pass #Private attributes.

    def reset_pass(self):
        print(self.__acc_pass)  #We can passes private methods and attributes directly so we take a another method to pass these value and execute it.

acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.rerset_pass())

class person:
    __name = "rohit"  #Private attributes.

    def __hello(self): # Private method.
        print("hello person!")
    
    def welcome(self): # A method to pass our private method.
        self.__hello()

p1 = person()     #hello person
print(p1.welcome())  #none

#Example of inheritance.

#Example of single inheritance..
class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Legender")
print(car1.stop())
print(car2.start())
 