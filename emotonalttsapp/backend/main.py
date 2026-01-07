from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import SessionLocal, engine
from models import Base, User, Script
from auth import hash_password, verify_password, create_token
from tts_engine import generate_tts
from audio_utils import get_audio_duration
from srt_generator import generate_srt
import asyncio
import os

Base.metadata.create_all(bind=engine)
app = FastAPI()

# --- ADD THIS SECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------

class Line(BaseModel):
    text: str
    emotion: str

class TTSRequest(BaseModel):
    gender: str
    lines: list[Line]

@app.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    db.add(User(email=email, password=hash_password(password)))
    db.commit()
    return {"msg": "registered"}

@app.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return {"error": "invalid"}
    return {"token": create_token(user.id)}

@app.post("/generate")
async def generate(req: TTSRequest):

    # 2. ADD THIS LINE TO CREATE THE FOLDER AUTOMATICALLY
    os.makedirs("output", exist_ok=True)
    
    audio_path = "output/audio.mp3"
    await generate_tts([l.dict() for l in req.lines], req.gender, audio_path)

    duration = get_audio_duration(audio_path)
    srt = generate_srt([l.text for l in req.lines], duration)

    with open("output/subtitles.srt", "w", encoding="utf-8") as f:
        f.write(srt)

    return {"audio": audio_path, "srt": "output/subtitles.srt"}
