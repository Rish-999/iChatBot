from fastapi import APIRouter
from model.request_models import QueryRequest
from services import chat_service


router = APIRouter(prefix="/chat",tags=["chat"])



@router.get("/start")
def start_chat_flow():return chat_service.get_start()
@router.get("/")
def root():return  chat_service.root()
@router.post("/respond")
def respond_chat_flow(req:QueryRequest): return  chat_service.get_response(req.query)