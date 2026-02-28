import json


# 1 example
print("JSON String -> Python Dict")
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)          # parse the JSON string
print(y)                   # dict
print(y["age"])            # 30


# 2 example
print("\n── Python Dict → JSON String ──")
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)
print(type(y))             # <class 'str'>


# 3 example
print("\n── Python Types → JSON ──")
print(json.dumps({"name": "John", "age": 30}))           # object
print(json.dumps(["apple", "bananas"]))                   # array
print(json.dumps(("apple", "bananas")))                   # array
print(json.dumps("hello"))                                # string
print(json.dumps(42))                                     # number
print(json.dumps(31.76))                                  # number
print(json.dumps(True))                                   # true
print(json.dumps(False))                                  # false
print(json.dumps(None))                                   # null


# 4 example
print("\n── Pretty-Printed JSON (indent=4) ──")
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=4))


# 5 example
print("\n── Sorted Keys ──")
print(json.dumps(x, indent=4, sort_keys=True))


# 6 example -> Read and Write
print("\n── Write & Read JSON File ──")
data = {"employees": [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob",   "dept": "Marketing"}
]}

# Write
with open("/tmp/data.json", "w") as f:
    json.dump(data, f, indent=4)
print("Written to /tmp/data.json")

# Read
with open("/tmp/data.json", "r") as f:
    loaded = json.load(f)
print("Read back:", loaded)
print("First employee:", loaded["employees"][0]["name"])
