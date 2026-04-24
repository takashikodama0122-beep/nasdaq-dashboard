import json

data = {
    "ndfd": 61.38,
    "net": 14,
    "ud": 1.00
}

with open("breadth.json", "w") as f:
    json.dump(data, f)

print("breadth.json updated")
