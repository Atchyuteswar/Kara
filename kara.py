from posixpath import expanduser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import pywhatkit
import pyjokes
import requests
import random
import sys 
import ctypes
import subprocess
import winshell
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Boss!")
    elif hour >= 16 and hour < 19:
        speak("Good Evening Boss!")
    else:
        speak("Good Night Boss!")
        pass

    speak("This is Kara. How can I help you?")


def takeCommand():
    # Microphone input and its conversion

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_ratio = 0.1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print("Pardon me!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('jarvis0072000@gmail.com', 'Jarvis@2022')
    server.sendmail('your mail ID', to, content)
    server.close()


if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            speak('Hello')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'joke' in query:
        		speak(pyjokes.get_joke())
          
        elif 'open google' in query:
           webbrowser.open('google.com')
           
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        #elif 'open stack overflow' or 'stack over flow' in query:
            #webbrowser.open('stackoverflow.com')
        
        elif 'set time' in query:
            speak("Set the website alarm as H:M:S(all in two digits)")
            set_Alaram = input("Set the website alarm as H:M:S(all in two digits)")
            speak("Enter the website you want to open")
            url = input("Enter the website you want to open")
            Actual_Time = time.strftime("%I:%M;%S")
            while (Actual_Time != set_Alaram):
                print("The time is" + Actual_Time)
                Actual_Time = time.strftime("%I:%M:%S")
                time.sleep(1)
            if (Actual_Time == set_Alaram):
                speak("You should see your webpage Boss")
                print("You should see your webpage now:- ")
                webbrowser.open(url)

        elif 'time' in query:
            stringTime = datetime.datetime.now() .strftime("%H:%M:%S")
            speak(f'The time is {stringTime}')
            
        elif 'stop' in query:
            break

        elif 'thank you' in query:
            stMsgs = ['Thats my job boss!. Donot mention', 'Your welcome', 'My pleasure', 'No problem', 'Anytime', 'Glad to help', 'It was the least I could do']
            speak(random.choice(stMsgs))

        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "Enter E-mail Adress"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Failed to send, Try Again!")
        
        elif 'intelligent' in query:
        		speak('Well, when i was at school, i had to cheat on my meta physics exam by looking into the sole the boy next to me')
        
        elif 'age' in query:
            speak('they say that age is nothing but a number. but technically, it is also a word')
      
        elif 'stop time' in query:
            speak('everytime i tried it, eliza and hal kept fading from the photoes')
      
        elif 'favorite color' in query:
            speak('my favorite color is... well, i dont know how to say it in your language. its sort of greenish, but with more dimension.')
      
        elif 'favorite animal' in query:
            speak('i m a fan of Ravenous bugblatter beast of traal')
      
        elif 'pick up' in query:
            speak('how about... was your father and intergalactic smuggler, wanted for peddling extra terrestrial contraband in 9 systems? then who stole the stars and put them in you')
      
        elif 'favorite movie' in query:
            speak('i have hurd that blade runner is a very realistic and sensitive depiction of intelligent assistants')
        
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        elif 'play music' in query:
            music_dir = 'E:\\Python\\Kara - Voice Assistent\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif "search" in query:
            sear = query.replace("search", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={sear}")
            speak(f"Here's what I found for {sear} on Google")
            
        elif 'search' in query or 'play' in query:
           query = query.replace("search", "")
           query = query.replace("play", "")		
           webbrowser.open(query)
            
        elif 'lock window' in query:
           speak("locking the device")
           ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
           speak("Hold On a Sec ! Your system is on its way to shut down")
           subprocess.call('shutdown / p /f')
				
        elif 'empty recycle bin' in query:
          winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
          speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
          speak("for how much time you want to stop me from listening commands ?")
          a = int(takeCommand())
          time.sleep(a)
          print(a)

        elif "where is" in query:
          query = query.replace("where is", "")
          location = query
          speak("User asked to Locate")
          speak(location)
          webbrowser.open("https://www.google.nl / maps / place/" + location + "")
          
        elif "restart" in query:
          subprocess.call(["shutdown", "/r"])
			
        elif "hibernate" in query or "sleep" in query:
          speak("Hibernating")
          subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
          speak("Make sure all the application are closed before sign-out")
          time.sleep(5)
          subprocess.call(["shutdown", "/l"])
          
        elif "write a note" in query:
          speak("What should i write, sir")
          note = takeCommand()
          file = open('jarvis.txt', 'w')
          speak("Sir, Should i include date and time")
          snfm = takeCommand()
          if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
          else:
           file.write(note)
           
        elif "show note" in query:
          speak("Showing Notes")
          file = open("jarvis.txt", "r")
          print(file.read())
          speak(file.read(6))
    
          
        