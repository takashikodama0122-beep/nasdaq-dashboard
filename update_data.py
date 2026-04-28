import json
import pandas as pd
import os
from datetime import datetime, timezone

prev = {}

if os.path.exists("breadth.json"):
    try:
        with open("breadth.json","r") as f:
            prev = json.load(f)
    except:
        pass

# Defaults
stack = prev.get("ema_stack","Mixed ⚠️")
atr_multiple = prev.get("atr",4.71)

try:
    url = "https://stooq.com/q/d/l/?s=qqq.us&i=d"
    df = pd.read_csv(url)

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna()

    close = df["Close"]

    last = close.iloc[-1]

    ema9 = close.ewm(span=9, adjust=False).mean().iloc[-1]
    ema21 = close.ewm(span=21, adjust=False).mean().iloc[-1]

    if last > ema9 and ema9 > ema21:
        stack = "Bullish ✅"
    elif last < ema9 and ema9 < ema21:
        stack = "Bearish ❌"
    else:
        stack = "Mixed ⚠️"

    tr = close.diff().abs()
    atr = tr.rolling(14).mean().iloc[-1]
    sma50 = close.rolling(50).mean().iloc[-1]

    atr_multiple = round((last - sma50) / atr,2)

except:
    pass

data = {
    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),

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
