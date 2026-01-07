def format_time(sec):
    ms = int((sec % 1) * 1000)
    s = int(sec) % 60
    m = int(sec // 60) % 60
    h = int(sec // 3600)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def generate_srt(lines, total_duration):
    total_words = sum(len(l.split()) for l in lines)
    time = 0.0
    srt = ""

    for i, line in enumerate(lines, 1):
        duration = (len(line.split()) / total_words) * total_duration
        srt += f"{i}\n{format_time(time)} --> {format_time(time+duration)}\n{line}\n\n"
        time += duration

    return srt
