from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import random
import time

app = FastAPI(title="TrendMonk AI API", version="1.0")

# Simulated vector database (mock)
TOKEN_DB = {
    "4RkRq...pump": {"score": 88.5, "wallets": 134, "mentions": 22},
    "XoPqA...bull": {"score": 91.2, "wallets": 155, "mentions": 37}
}

class TokenRequest(BaseModel):
    token: str

class ScoreResponse(BaseModel):
    token: str
    trend_score: float
    wallet_count: int
    social_mentions: int
    updated_at: float

@app.get("/")
def root():
    return {"message": "TrendMonk AI API is live."}

@app.get("/trend-score", response_model=ScoreResponse)
def get_trend_score(token: str = Query(..., description="Token mint address or hash")):
    if token not in TOKEN_DB:
        raise HTTPException(status_code=404, detail="Token not found")
    data = TOKEN_DB[token]
    return {
        "token": token,
        "trend_score": data["score"],
        "wallet_count": data["wallets"],
        "social_mentions": data["mentions"],
        "updated_at": time.time()
    }

@app.post("/trend-score", response_model=ScoreResponse)
def generate_score(req: TokenRequest):
    score = round(random.uniform(60, 99), 2)
    wallets = random.randint(50, 200)
    mentions = random.randint(5, 50)
    TOKEN_DB[req.token] = {
        "score": score,
        "wallets": wallets,
        "mentions": mentions
    }
    return {
        "token": req.token,
        "trend_score": score,
        "wallet_count": wallets,
        "social_mentions": mentions,
        "updated_at": time.time()
    }

@app.get("/top-tokens")
def get_top_tokens(limit: int = 5):
    sorted_tokens = sorted(TOKEN_DB.items(), key=lambda x: x[1]['score'], reverse=True)
    return [{"token": t[0], **t[1]} for t in sorted_tokens[:limit]]

@app.delete("/delete-token/{token_id}")
def delete_token(token_id: str):
    if token_id in TOKEN_DB:
        del TOKEN_DB[token_id]
        return {"status": "deleted", "token": token_id}
    raise HTTPException(status_code=404, detail="Token not found")
