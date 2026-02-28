import math
import random


# 1 example
print("── Built-in Math Functions ──")
print(min(5, 10, 25))     # 5
print(max(5, 10, 25))     # 25
print(abs(-7.25))         # 7.25
print(pow(4, 3))          # 64  (4³)


# 2 example
print("\n── math Module ──")
print(math.sqrt(64))      # 8.0
print(math.ceil(1.4))     # 2
print(math.floor(1.4))    # 1
print(math.pi)            # 3.141592653589793


# 3 example
print("\n── More math Functions ──")
print(math.factorial(5))  # 120
print(math.log(10))       # natural log
print(math.log10(1000))   # log base-10 → 3.0
print(math.gcd(12, 8))    # greatest common divisor → 4
print(math.isfinite(100))  # True
print(math.isinf(float('inf')))  # True


# 4 example
print("\n── Trigonometry ──")
print(math.sin(math.radians(90)))   # 1.0
print(math.cos(math.radians(0)))    # 1.0
print(math.tan(math.radians(45)))   # ≈1.0


# 5 example
print("\n── random Module ──")

# random integer in range
print("Random int (1–10)  :", random.randint(1, 10))

# random float between 0 and 1
print("Random float (0–1) :", random.random())

# random choice from a list
mylist = ["apple", "banana", "cherry"]
print("Random choice      :", random.choice(mylist))

# shuffle a list (in-place)
random.shuffle(mylist)
print("Shuffled list      :", mylist)

# random float in a given range
print("Uniform (1.5–9.5)  :", random.uniform(1.5, 9.5))

# random sample (no repeat)
print("Sample (2 of 1–10) :", random.sample(range(1, 11), 2))
