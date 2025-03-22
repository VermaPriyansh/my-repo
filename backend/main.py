# backend/app/main.py
from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import asyncio
import logging
import json

from app.core.prompt_processor import PromptProcessor
from app.services.cache_service import CacheService

app = FastAPI(title="AI Prompt Validator API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
cache_service = CacheService()
prompt_processor = PromptProcessor()

logger = logging.getLogger("api")

class PromptRequest(BaseModel):
    text: str
    source_language: Optional[str] = None
    target_language: Optional[str] = None
    options: Optional[Dict[str, Any]] = {}

class ValidationResponse(BaseModel):
    original_text: str
    validated_text: str
    issues: List[Dict[str, Any]]
    metrics: Dict[str, Any]
    suggestions: List[Dict[str, Any]]

@app.get("/")
async def root():
    return {"message": "AI Prompt Validator API"}

@app.post("/api/validate", response_model=ValidationResponse)
async def validate_prompt(request: PromptRequest):
    try:
        # Check cache first
        cache_key = f"{request.text}:{request.target_language}"
        cached_result = cache_service.get(cache_key)
        
        if cached_result:
            logger.info(f"Cache hit for prompt: {request.text[:30]}...")
            return cached_result
        
        # Process the prompt
        result = await prompt_processor.process(
            text=request.text,
            source_language=request.source_language,
            target_language=request.target_language,
            options=request.options
        )
        
        # Save to cache
        cache_service.set(cache_key, result)
        
        return result
    
    except Exception as e:
        logger.error(f"Error processing prompt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ws/validate")
async def websocket_validate(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            data = await websocket.receive_text()
            request_data = json.loads(data)
            
            request = PromptRequest(**request_data)
            result = await prompt_processor.process(
                text=request.text,
                source_language=request.source_language,
                target_language=request.target_language,
                options=request.options
            )
            
            await websocket.send_json(result.dict())
    
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        await websocket.close(code=1000)
