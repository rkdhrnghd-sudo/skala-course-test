from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello hackathon"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}
