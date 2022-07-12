from ast import Try
from logging import exception
from time import strftime
from unicodedata import name
from unittest import result
from winsound import PlaySound
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<15:
        speak("Good Afternoon")
    elif hour>=15 and hour<17:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("Hi i am zira, I am here to help you")   

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 2000  
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:,{query}\n") 

    except exception as e:
        print("Say that again...")
        return "None"  
    return query        

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()


        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("wikipedia says")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open browser' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}") 