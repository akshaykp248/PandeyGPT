from fastapi import FastAPI, HTTPException
from model import model

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM API!"}

@app.post("/generate/")
def generate(prompt: str, max_length: int = 200):
    try:
        response = model.generate_text(prompt, max_length)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
