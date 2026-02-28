import json


def loading() -> dict:
    with open("some_data.json", "r") as f:
        return json.load(f)


get_data = loading()


def get(x: dict):
    for i, value in x.items():
        if type(x[i]) == str:
            yield value
        elif type(x[i]) == dict:
            yield from get(value)
        else:
            continue


for i in get(get_data):
    print(i)
