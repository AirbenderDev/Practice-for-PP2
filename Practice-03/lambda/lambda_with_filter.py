# 1 example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# 2 example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 3 example
numbers = [5, 12, 17, 18, 24, 32]
greater_than_15 = list(filter(lambda x: x > 15, numbers))
print(greater_than_15)


# 4 example
words = ["apple", "banana", "kiwi", "cherry", "mango"]
short_words = list(filter(lambda x: len(x) < 6, words))
print(short_words)


# 5 example
numbers = [-5, -2, 0, 3, 7, -1, 8]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)
