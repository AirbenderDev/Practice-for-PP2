# 1 example
class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id


class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)


mgr = Manager("John", "E123")
print(mgr.name, mgr.employee_id)


# 2 example
class A:
    def method_a(self):
        print("Method from class A")


class B:
    def method_b(self):
        print("Method from class B")


class C(A, B):
    pass


obj = C()
obj.method_a()
obj.method_b()


# 3 example
class Father:
    def skills(self):
        print("Gardening, Programming")


class Mother:
    def skills(self):
        print("Cooking, Teaching")


class Child(Father, Mother):
    pass


child = Child()
child.skills()


# 4 example
class Animal:
    def eat(self):
        print("Eating...")


class Flyer:
    def fly(self):
        print("Flying...")


class Bat(Animal, Flyer):
    pass


bat = Bat()
bat.eat()
bat.fly()


# 5 example
class Walker:
    def walk(self):
        print("Walking")


class Swimmer:
    def swim(self):
        print("Swimming")


class Amphibian(Walker, Swimmer):
    pass


frog = Amphibian()
frog.walk()
frog.swim()
