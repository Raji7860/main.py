from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio
import edge_tts

app = FastAPI()

@app.get("/speak/")
async def speak(text: str):
    output_file = "output.mp3"
    tts = edge_tts.Communicate(text, voice="ms-fa-IR-FaridNeural")
    await tts.save(output_file)
    return FileResponse(output_file, media_type="audio/mpeg", filename="speech.mp3")

