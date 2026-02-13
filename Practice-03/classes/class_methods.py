# 1 example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# 2 example
class Calculator:
    def add(self, a, b):
        return a + b


calc = Calculator()
result = calc.add(5, 3)
print(result)


# 3 example
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Buddy")
dog1.bark()


# 4 example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(5, 10)
print(rect.area())


# 5 example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


account = BankAccount(100)
account.deposit(50)
print(account.get_balance())
