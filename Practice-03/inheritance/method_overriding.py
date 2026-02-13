# 1 example
class Person:
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname)


class Student(Person):
    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()


# 2 example
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()


# 3 example
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(5, 10)
print(rect.area())


# 4 example
class Vehicle:
    def drive(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road")


car = Car()
car.drive()


# 5 example
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is coding")


dev = Developer()
dev.work()
