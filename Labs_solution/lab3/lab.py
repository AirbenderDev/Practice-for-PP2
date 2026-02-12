# 1 example
import math
s = str(input())

isTrue = False

for i in s:
    if int(i) % 2 == 0:
        isTrue = True
    else:
        isTrue = False
        break

if isTrue:
    print("Valid")
else:
    print("Not valid")

# 2 example

x = int(input())


def isUsual(n: int) -> None:
    if n <= 0:
        print("No")
    else:
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p

        if n == 1:
            print("Yes")
        else:
            print("No")


isUsual(x)

# 3 example

my_dict = {
    "ONE": 1, "TWO": 2, "THR": 3, "FOU": 4, "FIV": 5,
    "SIX": 6, "SEV": 7, "EIG": 8, "NIN": 9, "ZER": 0
}

cmd = input()

for sign in "+-*":
    if sign in cmd:
        main_sign = sign
        break

left_str, right_str = cmd.split(main_sign)


def parse_number(s):
    num = ""
    for i in range(0, len(s), 3):
        num += str(my_dict[s[i:i+3]])
    return int(num)


a = parse_number(left_str)
b = parse_number(right_str)

if main_sign == "+":
    res = a + b
elif main_sign == "-":
    res = a - b
else:
    res = a * b

reverse = {}

for key in my_dict:
    reverse[my_dict[key]] = key

answer = ""
for d in str(res):
    answer += reverse[int(d)]

print(answer)

# 4 example

smth = input()
print(smth.upper())

# 5 example

smth = input()
print(smth**2)

# 6 example


class Rectangle:
    def __init__(self, n1, n2):
        self.length = n1
        self.width = n2

    def Shape(self):
        print(self.length * self.width)


length, width = map(int, input().split())

smth = Rectangle(length, width)
smth.Shape()

# 7 exmaple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return pow(dx * dx + dy * dy, 1/2)


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

p1 = Point(x1, y1)
p1.show()

p1.move(x2, y2)
p1.show()

p2 = Point(x3, y3)
distance = p1.dist(p2)

print(f"{distance:.2f}")

# 8 example


class Compare:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compare_smth(self):
        if self.x - self.y >= 0:
            print(self.x - self.y)
        else:
            print("Insufficient Funds")


x, y = map(int, input().split())
smth = Compare(x, y)
smth.compare_smth()

# 9 example


class Mult:
    def __init__(self, x):
        self.x = x

    def mult(self):
        area = 3.14159 * pow(self.x, 2)
        print(f"{area:.2f}")


smth = int(input())
smth1 = Mult(smth)
smth1.mult()


# 10 example

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")


name, gpa = input().split()
gpa = float(gpa)

student = Student(name, gpa)
student.display()

# 11 example


class Pair:
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2

    def pair_sum(self):
        a12 = self.a1 + self.a2
        b12 = self.b1 + self.b2
        print(f"Result: {a12} {b12}")


a1, b1, a2, b2 = map(int, input().split())
smth = Pair(a1, b1, a2, b2)
smth.pair_sum()

# 12 example


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary + self.base_salary * self.bonus_percent / 100


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500


class Intern(Employee):
    pass


data = input().split()
role = data[0]
name = data[1]

if role == "Manager":
    base_salary = int(data[2])
    bonus_percent = int(data[3])
    emp = Manager(name, base_salary, bonus_percent)

elif role == "Developer":
    base_salary = int(data[2])
    projects = int(data[3])
    emp = Developer(name, base_salary, projects)

else:  # Intern
    base_salary = int(data[2])
    emp = Intern(name, base_salary)

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")


# 13 example

prime = []


class PrimeNums:
    def __init__(self, x):
        self.x = x

    def Prime(self):
        for i in range(2, pow(i, i)+1 <= self.x):
            if x % i:
                break
            else:
                prime.append(self.x)


prime_input = input().split

for d in prime_input:
    a = int(d)
    smth = PrimeNums(a)
    smth.Prime

for d in prime:
    print(int(d), end=" ")


if prime:
    for d in prime:
        print(d, end=" ")
else:
    print("No primes")


# 14 example

n = int(input())
my_list = list(map(int, input().split()))
b = int(input())

for _ in range(b):
    c = input().split()
    if c[0] == "abs":
        my_list = [abs(u) for u in my_list]
    elif c[0] == "add":
        my_list = [u + int(c[1]) for u in my_list]
    elif c[0] == "power":
        my_list = [pow(u, int(c[1])) for u in my_list]
    elif c[0] == "multiply":
        my_list = [u * int(c[1]) for u in my_list]

print(*my_list)
