# 1 example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("Mike", "Olsen")
print(x.firstname, x.lastname)


# 2 example
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Buddy", "Golden Retriever")
print(dog.name, dog.breed)


# 3 example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car = Car("Toyota", "Camry")
print(car.brand, car.model)


# 4 example
class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


mgr = Manager("Alice", "IT")
print(mgr.name, mgr.department)


# 5 example
class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius


circle = Circle("Blue", 5)
print(circle.color, circle.radius)
