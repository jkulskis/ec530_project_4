from collections import deque
from factory import SpeechAudio

audio_queue = deque()
finished_audios = deque()


def add_audio(filepath: str):
    audio_queue.append(filepath)
    # use speech recognition to

def interpret_audios():
    while audio_queue:
        speech_audio = audio_queue.popleft()
        speech_audio.interpret()
        finished_audios.append(speech_audio)
    # all finished audios interpreted

if __name__ == "__main__":
    pass