# backend/models/request_models.py

from iChatBot.model.request_models import QueryRequest

from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

