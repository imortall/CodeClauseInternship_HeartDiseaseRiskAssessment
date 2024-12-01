import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyjokes
import keyboard
import pyautogui
from bs4 import BeautifulSoup
import requests
import geocoder
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')    

    speak('I am Jarvis how can help you')

def get_live_location():
    """Get the live location of the user."""
    g = geocoder.ip('me')  # Fetch live location using IP
    if g.ok:
        location = g.latlng
        speak(f"Your live location is Latitude {location[0]} and Longitude {location[1]}")
        print(f"Your live location is: {location}")
        return location
    else:
        speak("Sorry, I couldn't fetch your live location.")
        return None  

def check_battery_status():
    """Check the battery and charger status."""
    battery = psutil.sensors_battery()
    if battery is None:
        speak("Sorry, I couldn't fetch the battery status.")
        return

    percent = battery.percent
    charging = battery.power_plugged

    if charging:
        speak(f"The laptop is currently charging. Battery level is {percent} percent.")
        print(f"Charging: Yes, Battery Level: {percent}%")
    else:
        speak(f"Battery level is {percent} percent.")
        print(f"Charging: No, Battery Level: {percent}%") 

if __name__ == "_main_":
    wishMe()
    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in query:
            speak("ok sir opening facebook")
            webbrowser.open("https://www.facebook.com")

        elif 'close facebook' in query:
            speak('okay sir, closing facebook')
            os.system('taskkill /f /im chrome.exe')

        elif "open whatsapp" in query:
            speak("ok sir opening whatsapp")
            webbrowser.open("https://www.whatsapp.com")

        elif 'close whatsapp' in query:
            speak('okay sir, closing whatsapp')
            os.system('taskkill /f /im chrome.exe')

        elif 'open instagram' in query:
            speak("ok sir opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'close instagram' in query:
            speak('okay sir, closing instagram')
            os.system('taskkill /f /im chrome.exe')

        elif  'open youtube' in query:
            speak("ok sir opening youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'close youtube' in query:
            speak('okay sir, closing youtube')
            os.system('taskkill /f /im chrome.exe')

        elif 'open chrome' in query:
            speak("ok sir opening chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'close chrome' in query:
            speak('okay sir, closing chrome')
            os.system("taskkill /f /im chrome.exe")

        elif 'open google' in query:
            speak('ok sir opening google')
            webbrowser.open('https://www.google.co.in/')
            speak("sir, what shoul i search on google")
            cm = takecommand()
            webbrowser.open(f"https://www.google.co.in/{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919608880692", "hii", 8,31)

        elif 'youtube search' in query or ' search in youtube' in query:
            speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com////results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            speak("ok sir opening code")
            codepath = ("C:\\Users\\shahi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codepath)

        elif 'close code' in query:
            speak("okay sir, closing code")
            os.system("taskkill /f /im code.exe")

        elif 'jokes' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'pause' in query or 'play' in query:
            keyboard.press('space bar')


        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'ful screen' in query or 'full screen' in query in 'short screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'volume down' in query:
            pyautogui.press('volumedown')

        elif 'close this tab' in query:
            speak('ok sir close this tab')
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            speak('ok sir open new tab')
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            speak('ok sir open new window')
            keyboard.press_and_release('ctrl + n')

        elif 'down' in query:
            pyautogui.press('down')

        elif 'up' in query:
            pyautogui.press('up')

        elif 'temperature' in query:
            # search = 'temperature in delhi'
            # url = f"https://www.google.com/search?q={search}"
            # r = requests.get(url)
            # data = BeautifulSoup(r.text,"html.parser")
            # temp = data.find("div",class_="BNeawe").text
            # speak(f"current {search} is {temp}")
            speak("Tell Me The Name Of tHE Place ")

            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature}")

        elif "location" in query:
            get_live_location()

        elif "battery" in query:
            check_battery_status()

        elif "thank you" in query:
            speak("welcome sir")