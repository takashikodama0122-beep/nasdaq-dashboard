import json
import os

prev = {}

if os.path.exists("breadth.json"):
    try:
        with open("breadth.json","r") as f:
            prev = json.load(f)
    except:
        pass

data = {
    "ema_stack": "Bullish ✅",
    "ndfd": 61.38,
    "ndfd_prev": prev.get("ndfd",61.38),
    "net": 14,
    "net_prev": prev.get("net",14),
    "ud": 1.00,
    "ud_prev": prev.get("ud",1.00),
    "atr": 4.71,
    "atr_prev": prev.get("atr",4.71)
}

with open("breadth.json","w") as f:
    json.dump(data,f)

print(data)
