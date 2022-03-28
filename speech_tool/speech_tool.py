from collections import deque
from factory import SpeechAudio
import threading


class AudioQueue:
    def __init__(self, max_threads=3):
        self.max_threads = max_threads
        self.audio_queue = deque()
        self.processed_audios = deque()

    def add_audio(self, filepath: str):
        self.audio_queue.append(SpeechAudio(audio_file=filepath))
        # use speech recognition to

    def interpret_audios(self):
        threads_and_audios = []
        while self.audio_queue:
            for i in range(self.max_threads):
                speech_audio = self.audio_queue.popleft()
                threads_and_audios.append(
                    (threading.Thread(target=speech_audio.interpret), speech_audio)
                )
                threads_and_audios[-1][0].start()
                if not self.audio_queue:
                    break
            # wait for these threads to finish before starting new ones
            for thread, audio in threads_and_audios:
                thread.join()
                self.processed_audios.append(audio)


if __name__ == "__main__":
    audio_queue = AudioQueue()
    audio_queue.add_audio("audios/1.mp3")
    audio_queue.add_audio("audios/2.mp3")
    audio_queue.add_audio("audios/3.mp3")
    audio_queue.add_audio("audios/4.mp3")
    audio_queue.add_audio("audios/5.mp3")
    audio_queue.interpret_audios()
