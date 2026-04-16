import json as js

f = open("employees.json", "w")

def write():
    data = {
        "name": "shivanee",
        "age": 18,
        "address": "pune"
    }

    js.dump(data, f)

write()
f.close()
