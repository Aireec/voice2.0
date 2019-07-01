import pyttsx3
import os
import webbrowser
import speech_recognition as sr  #pip install speechRecognition
from selenium import webdriver
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.0
        audio = r.listen(source)

    try:
        print("Recognizing...")
        search = r.recognize_google(audio, language='en-in')
        print(f"User said: {search}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return search


def speak(text):
    engine.say(text)
    engine.runAndWait()

def google():
    speak('Opening google')
    speak('Any thing you want me to search')
    voiceI = takeCommand()


    browser = webdriver.Chrome()
    browser.get("http://www.google.com")
    input_element = browser.find_element_by_name("q")
    input_element.send_keys(voiceI)
    input_element.submit()


def close_browser():
    pyautogui.hotkey('alt', 'f4')