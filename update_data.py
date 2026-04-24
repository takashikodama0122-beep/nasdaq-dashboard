import json
import pandas as pd

url = "https://stooq.com/q/d/l/?s=qqq.us&i=d"

df = pd.read_csv(url)
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df = df.dropna()

close = df["Close"]

last_price = close.iloc[-1]
ema9 = close.ewm(span=9, adjust=False).mean().iloc[-1]
ema21 = close.ewm(span=21, adjust=False).mean().iloc[-1]

if last_price > ema9 and ema9 > ema21:
    stack = "Bullish ✅"
elif last_price < ema9 and ema9 < ema21:
    stack = "Bearish ❌"
else:
    stack = "Mixed ⚠️"

data = {
    "ema_stack": stack,
    "ndfd": 61.38,
    "net": 14,
    "ud": 1.00
}

with open("breadth.json", "w") as f:
    json.dump(data, f)

print(data)
