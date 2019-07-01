import random

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # r.pause_threshold = 0.0
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


def hello():
    speak("Greetings Sir")


def thank_you():
    thankU_Response = ['Your welcome', 'My Pleasure', 'At your service', 'Just doing my job', 'Can I get some sleep now',
                        'Do I get a raise']
    engine.say(random.choice(thankU_Response))
    engine.runAndWait()

def HAU():
    speak("Im fine, thank you for asking")