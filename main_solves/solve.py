import json


def loading() -> dict:
    with open("sample.json", "r") as f:
        return json.load(f)


my_dict = loading()


def get_data(x: dict):
    dn_str = x["imdata"][1]["l1PhysIf"]["attributes"]["dn"]
    mtu_str = x["imdata"][1]["l1PhysIf"]["attributes"]["mtu"]
    speed_str = x["imdata"][1]["l1PhysIf"]["attributes"]["speed"]
    yield dn_str, mtu_str, speed_str


for i in get_data(my_dict):
    print(i)
