from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio
import edge_tts
import os

app = FastAPI()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@app.get("/speak/")
async def speak(text: str):
    output_file = "/tmp/output.mp3"  
    tts = edge_tts.Communicate(text, voice="fa-IR-DilaraNeural")  
    await tts.save(output_file)  
    return FileResponse(output_file, media_type="audio/mpeg", filename="speech.mp3")

@app.get("/")
async def root():
    return {"message": "Welcome to the Text-to-Speech API! Use /speak/?text=YourText"}
