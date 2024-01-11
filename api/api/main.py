from fastapi import (FastAPI, Body, Depends, File, HTTPException, Query, UploadFile, Request, status)
from db import Base, engine
import models, schemas, crud, db
import requests
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return{
        "title":"Hello World!",
        "description":"FastAPIの勉強用サンプルプロジェクト"
        }
