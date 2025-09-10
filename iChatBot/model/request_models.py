# backend/models/request_models.py

from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str


