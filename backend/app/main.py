from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base,engine
import os

import app.models

app = FastAPI()
Base.metadata.create_all(bind=engine)

cors_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,https://dsaduel.ranker.app,https://www.dsaduel.ranker.app,https://dsaduel-api.ranker.app,https://www.dsaduel-api.ranker.app",
    ).split(",")
    if origin.strip()
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "hello world"}
