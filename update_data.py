import json
import pandas as pd
import os

url = "https://stooq.com/q/d/l/?s=qqq.us&i=d"

df = pd.read_csv(url)
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df = df.dropna()

close = df["Close"]

last_price = close.iloc[-1]

ema9 = close.ewm(span=9, adjust=False).mean().iloc[-1]
ema21 = close.ewm(span=21, adjust=False).mean().iloc[-1]

# EMA STACK
if last_price > ema9 and ema9 > ema21:
    stack = "Bullish ✅"
elif last_price < ema9 and ema9 < ema21:
    stack = "Bearish ❌"
else:
    stack = "Mixed ⚠️"

# ATR proxy
tr = close.diff().abs()
atr = tr.rolling(14).mean().iloc[-1]

# 50SMA
sma50 = close.rolling(50).mean().iloc[-1]

atr_multiple = round((last_price - sma50) / atr, 2)

# Load previous data if exists
prev = {}

if os.path.exists("breadth.json"):
    try:
        with open("breadth.json","r") as f:
            prev = json.load(f)
    except:
        prev = {}

data = {
    "ema_stack": stack,

    "ndfd": 61.38,
    "ndfd_prev": prev.get("ndfd",61.38),

    "net": 14,
    "net_prev": prev.get("net",14),

    "ud": 1.00,
    "ud_prev": prev.get("ud",1.00),

    "atr": atr_multiple,
    "atr_prev": prev.get("atr",atr_multiple)
}

with open("breadth.json","w") as f:
    json.dump(data,f)

print(data)
