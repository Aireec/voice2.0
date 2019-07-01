import pyttsx3
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def weather():
        driver = webdriver.Chrome()
        driver.get("https://www.weather-forecast.com/locations/Port-Elizabeth/forecasts/latest")
        weather = driver.find_element_by_class_name("b-forecast__table-description-content").text
        engine.say(weather)
        engine.runAndWait()

        driver.quit()