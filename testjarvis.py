#LETS GO IT FINALLY WORKS ALL OF IT

import os
import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import datetime
import math
import random

try:
    devices = AudioUtilities.GetSpeakers()
    volume_control = devices.EndpointVolume
except Exception as e:
    print("Volume controls failed to load. Error : " + str(e))
    volume_control = None

engine = pyttsx3.init() 

def speak(text):
    print("jarvis: " + text)
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=2)
    print("Jarvis online")

    with microphone as source:
        print("Calibrating mic for background noise... please stay quiet.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        recognizer.pause_threshold = 0.8

        speak("Hello Sir")
        time.sleep(1)

        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("processing audio...")
                text = recognizer.recognize_google(audio).lower()
                print("you said: " + text)
                
                if text == "jarvis thank you" or text == "thank you":
                    speak("You're welcome Sir")
                elif "jarvis" in text:
                    if "shut down" in text:
                        speak("Goodbye Sir")
                        break
                    reply(text)

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                print("... didnt catch that...")
            except sr.RequestError as e:
                print("Error: " + str(e))
            except KeyboardInterrupt:
                print("\nShutting down")
                break

def get_current_volume():
    if volume_control is None:
        return 50
    current_scalar = volume_control.GetMasterVolumeLevelScalar()
    return int(round(current_scalar * 100))

def set_volume_percentage(target):
    if volume_control is None:
        return target
    target = max(0, min(100, target))
    if target == 0:
        volume_control.SetMute(1, None)
    else:
        volume_control.SetMute(0, None)
        volume_control.SetMasterVolumeLevelScalar(target / 100.0, None)
    return target

def reply(text):
    words = text.split()
    if "open" in text:
        if "spotify" in text:
            speak("Opening Spotify")
            try:
                subprocess.Popen("start spotify:", shell=True)
            except Exception as e:
                print("Failed to open spotify: " + str(e))
                speak("I'm Sorry Sir, I could not open Spotify")
        elif "google" in text:
            speak("Opening Google")
            try:
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([chrome_path])
            except FileNotFoundError:
                print("file path not found")
        elif "email" in text:
            speak("Opening your email, Sir")
            webbrowser.open("https://gmail.com")
        elif "youtube" in text:
            speak("Sir, you know doomscrolling is bad for you, right?")
            webbrowser.open("https://youtube.com")
            
    elif "search for" in text:
        print("working")
        query = text.split("search for")[1].strip()
        if query == "":
            speak("It doesn't sound like you said anything, try again?")
        else:
            speak("Searching google for" + query)
            url = "https://www.google.com/search?q=" + query
            webbrowser.open(url)
        
    elif "volume" in text:
        numbers = [int(s) for s in words if s.isdigit()]
        amount = numbers[0] if numbers else 10
        current = get_current_volume()
        if "increase" in text or "up" in text:
            new = set_volume_percentage(current + amount)
            speak("Increasing Volume to " + str(new) + " percent")
        elif "decrease" in text or "down" in text:
            new = set_volume_percentage(current - amount)
            speak("Lowering Volume to " + str(new) + " percent")
        elif "set" in text or "to" in text:
            if numbers:
                new_vol = set_volume_percentage(amount)
                speak("Volume Capacity is at " + str(new_vol) + " percent")
            else:
                speak("Set it to what level sir?")

    elif "reminder" in text:
        if "to" in text:
            objective = text.split("to")[1].strip()
        elif "for" in text:
            objective = text.split("for")[1].strip()
        speak(objective)

    elif "current time" in text or "clock" in text:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak("The current time is " + current_time + ", Sir.")

    elif "date" in text or "today" in text:
        now = datetime.datetime.now()
        current_date = now.strftime("%B %d, %Y")
        speak("Today's date is " + current_date + ".")        

    elif "calculate" in text or "math" in text or "what is" in text:
        numbers = [int(s) for s in words if s.isdigit()]
        
        if len(numbers) >= 2:
            num1, num2 = numbers[0], numbers[1]
            if "plus" in text or "add" in text:
                result = num1 + num2
                speak("The answer is " + str(result))
            elif "minus" in text or "subtract" in text:
                result = num1 - num2
                speak("The answer is " + str(result))
            elif "times" in text or "multiply" in text or "multiplied by" in text:
                result = num1 * num2
                speak("The answer is " + str(result))
            elif "divide" in text or "divided by" in text:
                if num2 != 0:
                    result = num1 / num2
                    speak("The answer is " + str(result))
                else:
                    speak("I cannot divide by zero, Sir.")
            elif "power" in text or "exponent" in text:
                speak("the answer is " + str(num1 ^ num2))
        elif "square root" in text:
            result = math.sqrt(numbers[0])
            speak("The answer is " + str(result))
        else:
            speak("I can not calculate given only one number")
            
    elif "dice" in text:
        numbers = [int(s) for s in words if s.isdigit()]
        if len(numbers) >= 2:
            num1 = numbers[0]
            num2 = numbers[1]
            if "side" in text and text.find(str(num1)) > text.find(str(num2)):
                num1, num2 = num2, num1
            speak("rolling " + str(num2) + " dice of side " + str(num1))
            for i in range(num2):
                speak(str(random.randint(1, num1)))
        elif len(numbers) == 1:
            speak("rolled a " + str(numbers[0]) + " sided dice. Result is " + str(random.randint(1, numbers[0])))
        else:
            speak("rolled dice. Result is " + str(random.randint(1, 6)))
    elif ".com" in text or "dot com" in text:
            cleaned_text = text.replace("dot com", ".com")
            words = cleaned_text.split()
            url = None
            for word in words:
                if ".com" in word:
                    url = word
                    break
            if url:
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = "https://" + url
                speak("Navigating to " + url)
                webbrowser.open(url)
            else:
                speak("I heard a web address, but couldn't parse the URL, Sir. Try again")
if __name__ == "__main__":
    listen_for_wake_word()