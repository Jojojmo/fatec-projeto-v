from fastapi import FastAPI
from app.backend.Schemas import Message
from app.llm.Call_llm import make_guess

app = FastAPI()

@app.post("/hello", response_model=Message)
def hello(prompt: str):
    return {"message": make_guess(prompt)}