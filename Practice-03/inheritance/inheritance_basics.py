# 1 example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


# 2 example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    pass


dog = Dog("Buddy")
dog.speak()


# 3 example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    pass


my_car = Car("Toyota")
print(my_car.brand)


# 4 example
class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    pass


circle = Circle("Red")
print(circle.color)


# 5 example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    pass


manager = Manager("John", 5000)
print(manager.name, manager.salary)
