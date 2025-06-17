from openai import OpenAI
from app.config import settings
import tempfile
import os
from typing import Optional

class OpenAIService:
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in environment variables")
        
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def transcribe_audio(self, audio_data: bytes, file_extension: str = "webm") -> str:
        """
        Transcribe audio using OpenAI's Whisper API
        
        Args:
            audio_data: Raw audio data in bytes
            file_extension: File extension for the audio format (default: webm)
        
        Returns:
            Transcribed text
        """
        try:
            # Create a temporary file to store the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp_file:
                tmp_file.write(audio_data)
                tmp_file_path = tmp_file.name
            
            # Open the file and send to Whisper API
            with open(tmp_file_path, "rb") as audio_file:
                response = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            
            # Clean up the temporary file
            os.unlink(tmp_file_path)
            
            return response.strip()
        
        except Exception as e:
            # Clean up on error
            if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
            raise e

openai_service = OpenAIService()