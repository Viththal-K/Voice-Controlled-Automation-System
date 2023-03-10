import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning VK")
    elif hour>=12 and hour<17:
        speak("Good Afternoon VK")
    else:
        speak("Good Evening VK")
    
    speak("What do you want me to help you with")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print("Say that again please")
        return "None"
    
    return query


if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        if 'open google drive' in query:
            webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
        
        elif 'open bright space' in query:
            webbrowser.open("https://brightspace.nyu.edu/d2l/home")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Viththal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'thanks' in query:
            speak("Bye VK, see you around")
