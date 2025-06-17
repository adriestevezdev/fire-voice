from fastapi import FastAPI, UploadFile, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.services import openai_service
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.APP_NAME)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Fire Voice Backend API",
        "status": "running",
        "endpoints": {
            "transcribe": "/api/transcribe",
            "websocket": "/ws/transcribe"
        }
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile):
    """
    Transcribe audio file using OpenAI Whisper API
    
    Args:
        file: Audio file to transcribe
    
    Returns:
        Transcribed text
    """
    try:
        # Validate file type
        allowed_extensions = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
        file_extension = file.filename.split(".")[-1].lower() if "." in file.filename else "webm"
        
        if file_extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"File type not supported. Allowed types: {', '.join(allowed_extensions)}"
            )
        
        # Read file content
        audio_data = await file.read()
        
        if not audio_data:
            raise HTTPException(status_code=400, detail="Empty file provided")
        
        # Transcribe audio
        transcription = await openai_service.transcribe_audio(audio_data, file_extension)
        
        return {
            "transcription": transcription,
            "filename": file.filename,
            "size": len(audio_data)
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error transcribing audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error transcribing audio: {str(e)}")

@app.websocket("/ws/transcribe")
async def websocket_transcribe(websocket: WebSocket):
    """
    WebSocket endpoint for real-time audio transcription
    """
    await websocket.accept()
    try:
        while True:
            # Receive audio data
            data = await websocket.receive_bytes()
            
            # Transcribe audio
            try:
                transcription = await openai_service.transcribe_audio(data, "webm")
                await websocket.send_json({
                    "type": "transcription",
                    "text": transcription,
                    "status": "success"
                })
            except Exception as e:
                await websocket.send_json({
                    "type": "error",
                    "message": str(e),
                    "status": "error"
                })
    
    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        await websocket.close(code=1000)