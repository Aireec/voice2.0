import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def TodoList():
    with open('D:/vorce ark2/to_do_list.txt') as f:
        lines = f.readlines()
    engine.say(lines)
    engine.runAndWait()
    engine.runAndWait()