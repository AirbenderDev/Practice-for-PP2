# 1 example
class MyClass:
    x = 5


p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)


# 2 example
class Employee:
    company = "TechCorp"


emp1 = Employee()
emp2 = Employee()
print(emp1.company)
print(emp2.company)


# 3 example
class Counter:
    count = 0

    def increment(self):
        Counter.count += 1


c1 = Counter()
c2 = Counter()
c1.increment()
c2.increment()
print(Counter.count)


# 4 example
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Alice")
print(s1.school)
print(s1.name)


# 5 example
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand


car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.wheels)
print(car2.wheels)
