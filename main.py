from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.engine import analyze_match
from app.combos import combo_multi_matches, combo_same_match
from app.formatter import premium_message

app = FastAPI(title="Football Betting App")

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.post("/combo/multi")
def multi_combo(data: dict):
    matches = [analyze_match(m) for m in data["matches"]]
    combo = combo_multi_matches(matches)
    return premium_message(combo, stake=20)

@app.post("/combo/single")
def single_combo(data: dict):
    match = analyze_match(data["match"])
    combo = combo_same_match(match)
    return premium_message(combo, stake=25)
