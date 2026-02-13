# 1 example
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# 2 example
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# 3 example
words = ["hello", "world", "python"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)


# 4 example
temps_f = [32, 68, 100]
temps_c = list(map(lambda f: (f - 32) * 5/9, temps_f))
print(temps_c)


# 5 example
numbers = [1, 2, 3, 4, 5]
plus_ten = list(map(lambda x: x + 10, numbers))
print(plus_ten)
