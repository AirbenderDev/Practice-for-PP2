import re

text = open("raw.txt", encoding="utf-8").read()

pattern = r"\d+\.\n(.+?)\n([\d,]+) x ([\d\s,]+)\n([\d\s,]+)"

items = re.findall(pattern, text)

for name, qty, price, total in items:
    print(name.strip(), qty, price, total)
