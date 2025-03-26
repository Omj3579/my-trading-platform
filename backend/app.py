from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.data_feed import get_candlestick_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/candles/{symbol}")
def candles(symbol: str):
    return get_candlestick_data(symbol)