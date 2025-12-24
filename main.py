from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "app": "Football Betting App"}

@app.get("/health")
def health():
    return {"health": "ok"}
