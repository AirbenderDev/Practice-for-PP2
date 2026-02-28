# 1 example
class MyNumbers:
    """An iterator that returns numbers, starting with 1, and each sequence
    will increase by one (returning 1, 2, 3, 4, 5 ...)."""

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print("── Iterator Example ──")
print(next(myiter))   # 1
print(next(myiter))   # 2
print(next(myiter))   # 3
print(next(myiter))   # 4
print(next(myiter))   # 5


# 2 example -> StopIterration
class MyNumbersLimited:
    """Stop after 20 iterations."""

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass2 = MyNumbersLimited()

print("\n── StopIteration Example (1–20) ──")
for x in myclass2:
    print(x)


# 3 example
def my_gen():
    yield 1
    yield 2
    yield 3


print("\n── Simple Generator ──")
for val in my_gen():
    print(val)


# 4 example
def infinite_sequence():
    """Yields an infinite sequence of numbers (use with next() or limit)."""
    num = 0
    while True:
        yield num
        num += 1


print("\n── Generator with Loop (first 5 values) ──")
gen = infinite_sequence()
for _ in range(5):
    print(next(gen))


# 5 example
print("\n── Generator Expression ──")
squares_gen = (x * x for x in range(1, 6))
for sq in squares_gen:
    print(sq)
