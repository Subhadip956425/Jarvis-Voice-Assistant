import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
import wolframalpha
from plyer import notification
from pygame import mixer
import speedtest
from pywikihow import search_wikihow
from requests import get
import socket
import pywhatkit as kit 
import wikipedia 
import openai




from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_jarvisUI
import sys






# Password protection
for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

# GUI OF JARVIS
# from INTRO import play_gif
# play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

# Function for speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function for take input through microphone
    


# Function for alarm
import subprocess

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    try:
        subprocess.call(["python", "C:\\Users\\subha\\Desktop\\Final\\alarm.py"])
    except Exception as e:
        print(f"Error occurred: {e}")



# GUI
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommand(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Understanding...")
            query  = r.recognize_google(audio,language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query


    def TaskExecution(self):
        import pyautogui
        import time
        import requests
        from bs4 import BeautifulSoup
        speak("Welcome sir, I am jervis, How can I help you")
        while True:
            self.query = self.takeCommand().lower()
            if "wake up" in self.query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    self.query = self.takeCommand().lower()
                    if "go to sleep" in self.query:
                        speak("Ok sir , You can call me anytime")
                        break
                    elif "hello" in self.query or "how r u" in self.query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in self.query:
                        speak("that's great, sir")
                    elif "what is your name" in self.query:
                        speak("My name is Jervis")
                    elif "how are you" in self.query:
                        speak("Perfect, sir")
                    elif "thank you" in self.query:
                        speak("you are welcome, sir")
                    elif "ip address" in self.query:
                        hostname = socket.gethostname()    
                        ip = socket.gethostbyname(hostname)
                        print(f"Your ip address is {ip}")
                        speak(f"Your ip address is {ip}")
                    # Access phonme cemera
                    elif "open phone camera" in self.query:
                        import urllib.request
                        import cv2
                        import numpy as np
                        import time
                        URL = "http://192.168.146.247:8080/shot.jpg"
                        while True:
                            img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                            img = cv2.imdecode(img_arr, -1)
                            cv2.imshow('IPWebcam', img)
                            q = cv2.waitKey(1)
                            if q == ord("q"):
                                break

                        cv2.destroyAllWindows()

                    
                    elif 'open youtube' in self.query:  
                        speak("what you will like to watch ?") 
                        self.qrry = self.takeCommand().lower() 
                        kit.playonyt(f"{self.qrry}") 
                    elif 'close chrome' in self.query: 
                        os.system("taskkill /f /im chrome.exe") 


                    elif "close the application" in self.query:
                        pyautogui.hotkey("Alt","F4")
                        speak("Application closed")
                    elif "open command prompt" in self.query: 
                        os.system("start cmd") 
                    elif "close command prompt" in self.query: 
                        os.system("taskkill /f /im cmd.exe")
                    

                    # Hot key
                    elif 'maximize this window' in self.query or 'maximise the window' in self.query:
                        pyautogui.hotkey('alt', 'space') 
                        time.sleep(1) 
                        pyautogui.press('x') 
                    elif 'open new window' in self.query: 
                        pyautogui.hotkey('ctrl', 'n') 
                    elif 'open new tab' in self.query: 
                        pyautogui.hotkey('ctrl', 't') 
                    elif 'open incognito window' in self.query: 
                        pyautogui.hotkey('ctrl', 'shift', 'n')
                    elif 'minimise this window' in self.query or 'minimize the window' in self.query: 
                        pyautogui.hotkey('alt', 'space') 
                        time.sleep(1) 
                        pyautogui.press('n')
                    elif 'open history' in self.query: 
                        pyautogui.hotkey('ctrl', 'h') 
                    elif 'open downloads' in self.query: 
                        pyautogui.hotkey('ctrl', 'j') 
                    elif 'previous tab' in self.query: 
                        pyautogui.hotkey('ctrl', 'shift', 'tab') 
                    elif 'next tab' in self.query: 
                        pyautogui.hotkey('ctrl', 'tab') 
                    elif 'close tab' in self.query: 
                        pyautogui.hotkey('ctrl', 'w') 
                    elif 'close window' in self.query: 
                        pyautogui.hotkey('ctrl', 'shift', 'w')
                    elif 'clear browsing history' in self.query: 
                        pyautogui.hotkey('ctrl', 'shift', 'delete') 
                    elif 'open notification' in self.query: 
                        pyautogui.hotkey('win', 'n') 
                    elif 'close notification' in self.query: 
                        pyautogui.hotkey('win', 'n') 
                    elif "scroll down" in self.query: 
                        pyautogui.scroll(1000) 
                    elif "scroll up" in self.query:
                        pyautogui.scroll(-1000)



                    elif "close" in self.query:
                        import pyautogui
                        pyautogui.hotkey("ctrl","w")
                        speak("Closing sir")


                    elif 'type' in self.query: 
                        self.query = self.query.replace("type", "") 
                        pyautogui.write(f"{self.query}")
                    elif 'press enter' in self.query:
                        pyautogui.press('enter')



                    elif 'youtube search' in self.query: 
                        self.query = self.query.replace("youtube search", "") 
                        pyautogui.hotkey('alt', 'd') 
                        time.sleep(1) 
                        pyautogui.press('tab') 
                        pyautogui.press('tab') 
                        pyautogui.press('tab') 
                        pyautogui.press('tab') 
                        time.sleep(1) 
                        pyautogui.write(f"{self.query}", 0.1) 
                        pyautogui.press('enter')

                    elif 'google search' in self.query: 
                        self.query = self.query.replace("google search", "") 
                        pyautogui.hotkey('alt', 'd') 
                        pyautogui.write(f"{self.query}", 0.1) 
                        pyautogui.press('enter')


                    # Control system app
                    elif "open" in self.query:
                        from Dictapp import openappweb
                        openappweb(self.query)
                    # search in google
                    elif "google" in self.query:
                        from SearchNow import searchGoogle
                        searchGoogle(self.query)

                    # You Tube control
                    elif "youtube" in self.query:
                        from SearchNow import searchYoutube
                        searchYoutube(self.query)
                    elif "pause" in self.query:
                        import pyautogui
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in self.query:
                        import pyautogui
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute" in self.query:
                        import pyautogui
                        pyautogui.press("m")
                        speak("video muted")
                    elif "unmute" in self.query:
                        import pyautogui
                        pyautogui.press("m")
                        speak("video unmuted")

                    elif "volume up" in self.query:
                        from keyboard import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in self.query:
                        from keyboard import volumedown
                        speak("Turning volume down, sir")
                        volumedown()


                    elif "switch the window" in self.query:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")

                    # wikipidia
                    elif "wikipedia" in self.query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(self.query)

                    # Playing songs
                    elif "tired" in self.query:
                        speak("Playing your favourite songs, sir")
                        a = (1,2,3)
                        b = random.choice(a)
                        if b==1:
                            webbrowser.open("https://youtu.be/LeBMKCWBFDk?si=7NlB_neLEAm8PtCu")
                        if b==2:
                            webbrowser.open("https://youtu.be/KPk34_zCt-g?si=SN43_gtBIsIG6-S8")
                        if b==3:
                            webbrowser.open("https://youtu.be/ObYCUJ-u6Js?si=BrH511W9A0_B_UIJ")

                    # News
                    elif "news" in self.query:
                        from NewsRead import latestnews
                        latestnews()

                    # Calculator
                    elif "calculate" in self.query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc
                        self.query = self.query.replace("calculate","")
                        self.query = self.query.replace("jarvis","")
                        Calc(self.query)
                    # Whatsapp
                    elif "whatsapp" in self.query:
                        from Whatsapp import sendMessage
                        sendMessage()
                    # System shut down
                    elif "shutdown the system" in self.query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                        elif shutdown == "no":
                            break
                    # weather and temparature
                    elif "temperature" in self.query:
                        import requests
                        from bs4 import BeautifulSoup
                        search = "temperature in kolkata"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "weather" in self.query:
                        import requests
                        from bs4 import BeautifulSoup
                        search = "weather in kolkata"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    # alarm
                    elif "set an alarm" in self.query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")

                    elif "the time" in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"Sir, the time is {strTime}")

                    # Password change using voice
                    elif "change password" in self.query:
                        speak("What's the new password")
                        new_pw = input("Enter the new password\n")
                        new_password = open("password.txt","w")
                        new_password.write(new_pw)
                        new_password.close()
                        speak("Done sir")
                        speak(f"Your new password is{new_pw}")
                    # shedule my day
                    elif "schedule my day" in self.query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        self.query = self.takeCommand().lower()
                        if "yes" in self.query:
                            file = open("tasks.txt","w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in self.query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                    elif "show my schedule" in self.query:
                        from plyer import notification
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("ss.mp3")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                    # Open Any App Function
                    elif "launch" in self.query:
                        import pyautogui   
                        self.query = self.query.replace("launch","")
                        self.query = self.query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(self.query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

                    # Internet Speed Function
                    elif "internet speed" in self.query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()/1048576
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")

                    # IPL SCORE FUNCTION  
                    elif "ipl score" in self.query:
                        from plyer import notification  #pip install plyer
                        import requests #pip install requests
                        from bs4 import BeautifulSoup #pip install bs4
                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text,"html.parser")
                        team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                        team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                        team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                        a = print(f"{team1} : {team1_score}")
                        b = print(f"{team2} : {team2_score}")

                        notification.notify(
                            title = "IPL SCORE :- ",
                            message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout = 15
                        )
                    # ROCK PAPER SCISSOR
                    elif "game" in self.query:
                        from game import game_play
                        game_play()

                        #SCREENSHOT FUNCTION
                    elif "screenshot" in self.query:
                        import time
                        import pyautogui
                        speak("Sir please tell me the name for this screeshot file")
                        name = self.takeCommand().lower()
                        speak("Sir please hold the screen for few seconds, I am taking the screenshot")
                        time.sleep(3)
                        im = pyautogui.screenshot()
                        im.save(f"{name}.jpg")
                        speak("Done sir")

                    #CAMERA FUNCTION
                    elif "click my photo" in self.query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    #FOCUS MODE FUNCTION
                    elif "focus mode" in self.query:
                        import subprocess
                        speak("Are you sure that you want to enter focus mode :- Type [1 for YES / 2 for NO ")
                        a = int(input())
                        if (a==1):
                            speak("Entering the focus mode....")
                            subprocess.call(["python", "C:\\Users\\subha\\Desktop\\Final\\FocusMode.py"])
                            exit()

                        
                        else:
                            pass

                    #FOCUS GRAPH FUNCTION
                    elif "show my focus" in self.query:
                        from FocusGraph import focus_graph
                        focus_graph()

                    # Translate function
                    elif "translate" in self.query:
                        from Translator import translategl
                        self.query = self.query.replace("jarvis","")
                        self.query = self.query.replace("translate","")
                        translategl(self.query)


                        
                    # To remember anything
                    elif "remember that" in self.query:
                        rememberMessage = self.query.replace("remember that","")
                        rememberMessage = self.query.replace("jarvis","")
                        speak("You told me to remember that"+rememberMessage)
                        remember = open("Remember.txt","a")
                        remember.write(rememberMessage)
                        remember.close()
                    elif "what do you remember" in self.query:
                        remember = open("Remember.txt","r")
                        speak("You told me to remember that" + remember.read())
                    
                    # CheckBettery Perceantage
                    elif "how much power" in self.query or "battery" in self.query:
                        import psutil
                        bettery = psutil.sensors_battery()
                        percentage = bettery.percent
                        speak(f"Sir our system have {percentage} percent battery")
                        if percentage >= 75:
                            speak("We have enough power to continue our work")
                        elif percentage >= 40 and percentage <= 75:
                            speak("We should connect our system to charging point to charge our battery")
                        elif percentage <= 15 and percentage <= 30:
                            speak("We don't have enough power to work, please connect to charging")
                        elif percentage <= 15:
                            speak("Sir we have very low power, please connect to charging the system, else system will shutdown very soon")

                    
                    
                    # To search anything
                    elif "activate how to do mode" in self.query:
                        speak("How to do mode is activated")
                        while True:
                            speak("Please tell me what you want to know")
                            how = self.takeCommand()
                            try:
                                if "exit" in how or "class" in how:
                                    speak("Okay sir, how to do mode is closed")
                                    break
                                else:
                                    max_results = 1
                                    how_to = search_wikihow(how, max_results)
                                    assert len(how_to) == 1
                                    how_to[0].print()
                                    speak(how_to[0].summary)

                            except Exception as e:
                                speak("Sorry sir, I am not able to find this")

                    elif "turn off" in self.query:
                        speak("Going to sleep, sir, You can call me anytime")
                        exit()
                    


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\subha\\Desktop\\Final/GIF from GIFER.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\subha\\Desktop\\Final/00545cb7179c504433d4c8f5e845f286.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\subha\\Desktop\\Final/ava_ai.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()



    def showTime(self):
        current_Time = QTime.currentTime()
        current_Date = QDate.currentDate()
        label_Time = current_Time.toString('hh:mm:ss')
        label_Date = current_Date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_Date)
        self.ui.textBrowser_2.setText(label_Time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())
