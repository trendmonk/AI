from fastapi import FastAPI
app = FastAPI()

@app.get("/trend-score")
def get_trend_score(token: str):
    return {"token": token, "score": 89.5}
