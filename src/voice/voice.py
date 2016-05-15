import speech_recognition as sr
import time
from src.parse.parse import Parse

class Voice:
    def __init__(self):
        self.keyphrase = "Jarvis"
        self.query = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = None

    def set_keyphrase(self, keyphrase):
        self.keyphrase = keyphrase

    def set_language(self, language):
         self.language = language


    def calibrate(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Calibrated")
            return self.recognizer

    def backgroundrecognition(self):

        def callback(recognizer, audio):
            try:
                result = self.recognizer.recognize_google(audio, show_all=False)

                if self.keyphrase in result:
                    result = result.replace(str(self.keyphrase),"",1)
                    self.query = result
                    # move start of parsing to main (with callback if self.query gets updated)
                    parse = Parse(self.query)

                else:
                    print("No keyphrase")
            except sr.RequestError as e:
                print(e)
                return e
            except sr.UnknownValueError as u:
                print(u)
                return u

        self.recognizer = self.calibrate()
        print("Background recognition now active")

        stop_listening = self.recognizer.listen_in_background(self.microphone, callback)

        # stop_listening()
        while True:
            time.sleep(0.1)
