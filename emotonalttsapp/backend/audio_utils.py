from pydub import AudioSegment
import os

# 1. Get the current folder path (where audio_utils.py is)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Tell pydub to use the ffmpeg/ffprobe files in this folder
AudioSegment.converter = os.path.join(current_dir, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(current_dir, "ffprobe.exe")

def get_audio_duration(path):
    return AudioSegment.from_file(path).duration_seconds
