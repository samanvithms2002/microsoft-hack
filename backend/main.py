import logging
import os
import uvicorn
from app.api.routers.chat import chat_router
from app.api.routers.nodeurl import nodeurl_router
from app.api.routers.controllers.fetch_topics_controller import fetch_topics_router
from app.api.routers.controllers.upload_document_controller import upload_documents_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set


if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(chat_router, prefix="/api/chat")
app.include_router(nodeurl_router, prefix= "/api/nodeurl")
app.include_router(fetch_topics_router, prefix="/api/topics")
app.include_router(upload_documents_router, prefix= "/api/document")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
