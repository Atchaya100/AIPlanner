from fastapi import APIRouter
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()
router = APIRouter()
# from groq import Groq



# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

class PromptRequest(BaseModel):
    prompt: str


# @router.post("/ask")
# async def ask_openai(data: PromptRequest):
#     try:
#         response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": data.prompt,
#         }
#     ],
#     model="llama-3.3-70b-versatile",
#     )
#         return {"response": response.choices[0].message.content}
#     except Exception as e:
#         return {"error": str(e)}


import requests

url = "https://api.perplexity.ai/chat/completions"

@router.post("/ask")
async def ask_openai(data: PromptRequest):
    try:
        payload = {
              "model": "sonar",
              "messages": [
                    {
                        "role": "system",
                        "content": "Be precise and concise."
                    },
                    {
                        "role": "user",
                        "content": data.prompt
                    }
                    ]
                }
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
            }
        response = requests.request("POST", url, json=payload, headers=headers)
        
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}


