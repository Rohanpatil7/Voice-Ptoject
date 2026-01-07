import edge_tts
from emotion_ai import detect_emotion_ml

def detect_language(text):
    return "hi" if any("\u0900" <= c <= "\u097F" for c in text) else "en"

def select_voice(text, gender):
    lang = detect_language(text)
    if lang == "hi":
        return "hi-IN-SwaraNeural" if gender == "female" else "hi-IN-MadhurNeural"
    return "en-IN-NeerjaNeural" if gender == "female" else "en-IN-PrabhatNeural"

async def generate_tts(lines, gender, out_file):
    voice = select_voice(lines[0]["text"], gender)
    ssml = f'<speak><voice name="{voice}">'

    for l in lines:
        emotion = l["emotion"]
        if emotion == "auto":
            emotion = detect_emotion_ml(l["text"])
        ssml += f"<emotion style='{emotion}'>{l['text']}</emotion><break time='600ms'/>"

    ssml += "</voice></speak>"
    await edge_tts.Communicate(ssml, voice).save(out_file)
