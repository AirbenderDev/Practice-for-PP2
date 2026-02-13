# 1 example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)


# 2 example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")
print(my_car.brand)


# 3 example
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


student1 = Student("Alice", 90)
print(f"{student1.name} - {student1.grade}")


# 4 example
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = Book("Python Guide", "John Doe")
print(book1.title)


# 5 example
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14


circle1 = Circle(5)
print(circle1.radius)
print(circle1.pi)
