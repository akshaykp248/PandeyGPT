from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import model

app = FastAPI()

# Define the request body model
class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 200

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM API!"}

@app.post("/generate/")
def generate(request: GenerateRequest):
    try:
        response = model.generate_text(request.prompt, request.max_length)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
