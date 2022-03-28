class SpeechAudio:

    def __init__(self, audio_file: str):
        self.audio_file = audio_file
        self.text = None
    
    def interpret(self):
        print(self.audio_file)
        pass # interpret the speech here
    
    @property
    def completed(self) -> bool:
        return self.text is not None

    def __repr__(self):
        return self.text if self.text is None else "None"