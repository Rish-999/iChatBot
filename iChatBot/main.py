from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from router import chat_router

app = FastAPI(title="iChatBot")

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
# ✅ Allow frontend to talk with backend
origins = [
    "http://localhost:52221",  # Flutter web dev server
    "http://127.0.0.1:52221",  # sometimes dev server binds here
    "http://localhost:8222",
    "http://127.0.0.1:8222",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for dev
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include routers
app.include_router(chat_router.router)










# from fastapi import FastAPI
# from pydantic import BaseModel
# from openai import OpenAI
# from openai.types.chat import ChatCompletionMessageParam
# import os
#
# app = FastAPI()
#
# # Configure OpenRouter client
# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY", "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")
# )
#
# class ChatRequest(BaseModel):
#     message: str
#
# @app.get("/")
# def root():
#     return {"status": "ok", "message": "FastAPI server is running 🚀"}
#
#
# @app.get("/ping")
# def ping():
#     return {"message": "pong"}
#
#
# @app.post("/chatAi")
# def chat(req: ChatRequest):
#     try:
#         # Explicitly declare type for messages
#         messages: list[ChatCompletionMessageParam] = [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": req.message},
#         ]
#
#         response = client.chat.completions.create(
#             model="mistralai/mistral-7b-instruct",
#             messages=messages,
#         )
#         reply = response.choices[0].message.content
#         return {"reply": reply}
#     except Exception as e:
#         return {"error": str(e)}
