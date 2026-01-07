from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

def detect_emotion_ml(text):
    label = classifier(text)[0]["label"]
    return {
        "joy": "cheerful",
        "anger": "angry",
        "sadness": "sad",
        "fear": "serious",
        "neutral": "calm"
    }.get(label, "confident")
