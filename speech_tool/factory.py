import speech_recognition as sr


class SpeechAudio:
    def __init__(self, audio_file: str):
        self.audio_file = sr.AudioFile(audio_file)
        self.recognizer = sr.Recognizer
        self.audio = None
        self.text = None

    def interpret(self):
        with audio_file as source:
            audio = self.recognizer.record(source)  # read the entire audio file
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + self.text := self.recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    @property
    def completed(self) -> bool:
        return self.text is not None

    def __repr__(self):
        return self.text if self.text is None else "None"
