# 1 example
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# 2 example
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# 3 example
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# 4 example
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# 5 example
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
