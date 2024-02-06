from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import requests
import asyncio

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

MODEL_URL = "https://api-inference.huggingface.co/models/bartowski/Michel-13B-exl2"

semaphore = asyncio.Semaphore(value=50)  # Set maximum number of concurrent requests

async def generate_chat_response(payload: dict) -> str:
    async with semaphore:
        try:
            response = requests.post(MODEL_URL, json=payload)
            response.raise_for_status()
            answer = response.json()["generations"][0]["answers"][0]["answer"]
            return answer
        except requests.exceptions.RequestException:
            raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, min_time_ms: Optional[int] = 500, max_concurrent_requests: Optional[int] = 5):
    tasks = []
    for _ in range(max_concurrent_requests):
        payload = {
            "inputs": {
                "session_id": "YOUR_SESSION_ID",
                "question": request.question
            }
        }
        tasks.append(generate_chat_response(payload))
        await asyncio.sleep(min_time_ms / 1000)
    answers = await asyncio.gather(*tasks)
    return ChatResponse(answer=answers)