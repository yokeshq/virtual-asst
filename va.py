from selenium import webdriver
import pyttsx3
import os

pyttsx3.speak(
    "Hello , I  am  terra , your  virtual  assistant  , Chat with me  your  requirements   ")

print("Welcome ,   \n I can run the following programs for you : \n Run chrome. \n Run vlc. \n Play music \n Run windows media player. \n Run notepad . \n Open gmail  \n Open youtube \n Open Calculator \n Open facebook \n If you wish to quit press'q' .")

while True:

    print("chat with me with your requirements : ", end=' ')

    p = input()

    if(("run" in p) or ("open" in p)) and ("chrome" in p):
        pyttsx3.speak("Opening chrome ")
        os.system("chrome")

    if (("dont run" in p) or ("dont open" in p)):
        pyttsx3.speak("Please specify the program you want to open ")

    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("Opening notepad ")
        os.system("start notepad")

    elif(("run" in p) or ("open" in p)) and ('youtube' in p):
        pyttsx3.speak("Opening youtube")
        driver = webdriver.Chrome()
        driver.get('https://youtube.com')

    elif(("run" in p) or ("open" in p) or ("send" in p)) and (('gmail' in p) or ('mail' in p)):
        pyttsx3.speak("Opening gmail ")
        driver = webdriver.Chrome()
        driver.get('https://gmail.com')

    elif(("run" in p) or ("open" in p)) and (("facebook" in p) or ("fb" in p)):
        pyttsx3.speak("Opening facebook ")
        driver = webdriver.Chrome()
        driver.get('https://facebook.com')

    elif ("run" in p) and ("player" in p) and ("media" in p):
        pyttsx3.speak("Opening  media player ")
        os.system("wmplayer")

    elif (("run" in p) or ("open" in p)) and ("vlc" in p):
        pyttsx3.speak("Opening vlc")
        os.system("start VLC")

    elif (("run" in p) or ("open" in p)) and ("calculator" in p):
        pyttsx3.speak("Opening calculator ")
        os.system("start calc")

    elif (("play" in p) or ("open" in p)) and (("music" in p) or ("song" in p)):
        pyttsx3.speak("Opening spotify , enjoy your  music ")
        os.system("spotify")

    elif (("exit" in p) or ("quit" in p) or ("q" in p) or ("bye" in p)):
        pyttsx3.speak("Bye then , Contact me when you need something  ")
        break

    else:
        pyttsx3.speak(
            "Sorry  this is not the specified command , Check the command  ")
        print("Sorry!,This command is not supported ")
