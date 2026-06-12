from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DevPulse is alive!", "status": "running"}

