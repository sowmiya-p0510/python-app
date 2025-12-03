# backend/routes/routes.py
"""
Main routes file - includes agent processing routes
Import other routers (claim_routes, hitl_routes, user_routes) in app.py
"""
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
def welcome():
    return {"message": "Welcome to the Real-estate"}