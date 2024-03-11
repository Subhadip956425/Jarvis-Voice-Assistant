import pyttsx3
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

# Function for speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function for wish
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon ,sir")

    elif hour >= 18 and hour < 22:
        speak("Good Evening,sir")
    else:
        speak("Sir, it's too late You may sleep now")

    speak("Please tell me, How can I help you sir?")