from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Choose a free open-source model (here: Mistral 7B Instruct, quantized smaller versions also exist)
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",   # automatically use GPU if available
    torch_dtype=torch.float16,  # reduce memory usage
)

# Function to chat
def chat(query: str):
    inputs = tokenizer(query, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test
print(chat("Hello, how are you?"))

# from fastapi import FastAPI
# from pydantic import BaseModel
# import cohere
#
# app = FastAPI()
# co = cohere.Client("uww8Np23ARAw0iWuohGncu2eCWmr8Ko2kBf2ofXw")  # replace with your actual key
#
# # In-memory history (per user you might want to use a DB or Redis)
# chat_history = []
#
# class ChatRequest(BaseModel):
#     message: str
#
#
#
# @app.post("/chat")
# def chat(req: ChatRequest):
#     try:
#         global chat_history
#
#         response = co.chat(
#             model="command-r",
#             message=req.message,
#             chat_history=chat_history,  # send past conversation
#         )
#
#         # Update history with this turn
#         chat_history = response.chat_history
#
#         return {
#             "reply": response.text,
#             "chat_history": chat_history  # optional: send back full history
#         }
#     except Exception as e:
#         return {"error": str(e)}
#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