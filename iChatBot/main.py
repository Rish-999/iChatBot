from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from router.chat_router import router as chat_router   # ✅ fixed

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

