from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request model
class QueryRequest(BaseModel):
    query: str


# Example flow tree
chat_flow = {
    "start": {
        "message": "Hello! What do you want help with?",
        "options": ["Order Status", "Refund", "Tech Support", "Machine Errors"]
    },
    "Order Status": {
        "message": "Please provide your order ID.",
        "options": [],
    },
    "Refund": {
        "message": "Refunds take 5-7 business days. Do you want policy details?",
        "options": ["Yes", "No"],
    },
    "Yes": {
        "message": "Refund policy: All returns must be postmarked within 30 days of the purchase date. All returned items must be in new and unused condition"
                   "Sale items are considered final sale and cannot be returned for a refund.",
        "options": ["start"]
    },
    "No": {
        "message": "Okay, anything else?",
        "options": ["Order Status", "Tech Support", "Machine Errors Resolve"]
    },
    "Machine Errors": {
        "message": "Please provide the error id",
        "options": ["001121", "100211", "101212", "101112"]
    },
    "001121":
        {
            "message": "The Machine might need restart.",
            "options": ["100211", "101212", "101112"]
        },
    "100211":
        {
            "message": "The Machine is at low memory, increase the memory size",
            "options": ["001121","101212", "101112"]
        },
    "101212":
        {
            "message": "The Machine weighing scale is taking default value, please reset the machine from setting panel",
            "options": ["001121", "100211","101112"]
        },
    "101112":
        {
            "message": "The Machine is at voltage fluctuations, please check the current supply",
            "options": ["001121", "100211", "101212"]
        }

}


@app.get("/chat/start")
def start_chat():
    return chat_flow["start"]


@app.post("/chat/respond")
def respond(req: QueryRequest):
    return chat_flow.get(req.query, {"message": "I don’t understand.", "options": []})
