# 1 example
def my_function(*args):
    print("Arguments:", args)
    print("First:", args[0])


my_function("Emil", "Tobias", "Linus")


# 2 example
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))


# 3 example
def my_function(**kwargs):
    print("His last name is " + kwargs["lname"])


my_function(fname="Tobias", lname="Refsnes")


# 4 example
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


print_info(name="John", age=30, city="New York")


# 5 example
def mixed_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


mixed_args(1, 2, 3, name="Alice", age=25)
