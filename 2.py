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

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys

from mainGUIFile import Ui_Dialog


class mainFile(QDialog):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Setting up GUI")
        self.firstUI = Ui_Dialog()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("C:\\Users\\subha\\Desktop\\Final/jarvisfullgui.gif")
        self.firstUI.mainGIF.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.ExitButton_3.clicked.connect(self.close)
        self.firstUI.StartButton.clicked.connect(self.connectToLoginWindow)
        self.firstUI.LoginButton_2.clicked.connect(self.connectToLoginWindow)
        #self.firstUI.StartButton.clicked.connect(self.connectToFaceRecognition)

    # def connectToFaceRecognition(self):
    #     from faceRECOG import faceRECOG
    #     self.showFaceRecogwindow = faceRECOG()
    #     ui.close()
    #     self.showFaceRecogwindow.show()
        
    def connectToLoginWindow(self):
        from loginWindowMAIN import loginWindow
        self.showLoginWindow.show()

    


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
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Understanding...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Function for alarm
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

    
if __name__ == "__main__":
    while True:
        app = QApplication(sys.argv)
        ui = mainFile()
        ui.show()
        sys.exit(app.exec_())
        
        
        