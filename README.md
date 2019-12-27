# voice2.0
voice controlled speech recognition controlling pc
python built
Libraries
#pyssx3
#selenuim
#speech recognition

*Greeting Responses.py*
Script that randomly selects from a preset list of greetings
Greeting triggers include words like: "Hello", "Thank You", "How are you".

*Question.py*
Script that allows automated google searchers.
Triggered by serach key word. A.I will ask for what you want to search for and enter your next word/phrase into the google search bar.
Using the selenium webdriver to automate the web pages

*To_do_list.py*
Script that reads to do list from a pre-written txt file.

*Voice.py* 
The meat and potatoes of the A.I. First function is the greet the user based on time of day e.g.(Morning or afternoon).
Second function to take in the next command spoken from user, interperate it, then compare results to the list of commands.
"if" and "else" statements that A.I will compare voice results to and execute the closest corresponding commmand.
Commands are to exectuted from main Voice.py Each command runs the correspoding py script.

*weather.py*
Weather.py script uses selenuim wed driver to automatically open weather website and read the weather forecast after which the webpage will be closed.


*REQUIRMENTS*
_pyttsx3_ 
Allows pc to speak out loud

_selenium web driver_
Alloows web pages to be automated
