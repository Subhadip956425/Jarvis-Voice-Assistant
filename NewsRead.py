import requests
import json
import pyttsx3
import speech_recognition


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=8b270f857c0c44d981c83d836ed5b9cc",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=8b270f857c0c44d981c83d836ed5b9cc",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=8b270f857c0c44d981c83d836ed5b9cc",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=8b270f857c0c44d981c83d836ed5b9cc",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=8b270f857c0c44d981c83d836ed5b9cc",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=8b270f857c0c44d981c83d836ed5b9cc"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takeCommand().lower()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")