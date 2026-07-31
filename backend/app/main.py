from fastapi import FastAPI

app = FastAPI(
    title="Aurora",
    description="An adaptive conversational AI.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "project": "Aurora",
        "status": "running",
        "message": "Welcome to Aurora."
    }