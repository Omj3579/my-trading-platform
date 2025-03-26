import pandas as pd

def get_candlestick_data(symbol: str):
    try:
        df = pd.read_csv(f"./backend/data/{symbol.upper()}.csv")
        candles = [
            {
                "time": int(pd.to_datetime(row["Date"]).timestamp()),
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "close": float(row["Close"])
            }
            for _, row in df.iterrows()
        ]
        return candles
    except Exception as e:
        return {"error": str(e)}
