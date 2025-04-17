from .constants import *

def transcribe(dir_name, video_filename):
    dir_path = os.path.join("uploads", dir_name)
    video_path = os.path.join(dir_path, video_filename)
    audio_path = os.path.join(dir_path, "extracted-audio.wav")

    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)

    transcript_path = os.path.join(dir_path, "transcript.txt")
    with open(transcript_path, "w") as file:
        file.write(transcript.text)
    return True

