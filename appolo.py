import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import subprocess
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

    

greetMe()


speak('Hi sargam, my name is apollo!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sargam! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your_email','Your_password') #enter your Email id and password
    server.sendmail('Your_email',to,content)
    server.close()


        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hey, the time is {strTime}")
                                                    
            
        elif 'open code' in query:
            speak('okay')
            pathw="C:\\Users\\Sargam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #enter the target location of your VS code
            os.startfile(pathw)

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "all good" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!, thanks for asking', 'great , its a good day afterall', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            speak('hope you are doing good as well')
            
        elif 'email' in query:
            try:
               speak("what should i say?")
               content = myCommand()
               to = input("enter the email of receiver:")
               sendemail(to,content)
               speak("email has been sent!")
            
            except Exception as e :
                 print(e)
                 speak("sorry sargam. i am not able to send your email right now")


           
        elif 'hello' in query:
            speak('Hello sargam , hope you are having a good day !')

                                    
        elif 'play music' in query:
            music_folder = r"C:\\Users\\hp\\Desktop\\audios" #enter path to your audio folder
            songs = os.listdir(music_folder)
            print(songs)
            os.startfile(os.path.join(music_folder,songs[0]))
                  
            speak('Okay, here is your music! Enjoy!')

        elif 'wikipedia' in query:
            speak("searching your query..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in query:
            subprocess.call('notepad.exe')

        elif 'open whatsapp' in query:
            subprocess.call('C:\\Users\\Sargam\\AppData\\Local\\WhatsApp\\WhatsApp.exe') #enter whatsapp target location

        elif 'open calculator' in query:
           subprocess.call('calc.exe')

        elif 'temperature' in query :
            search = "temperature in jammu and kashmir"
            url = f" https://www.google.com/search?q={search}"
            x=requests.get(url)
            data = BeautifulSoup(x.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")


        elif 'bye' or 'exit' in query:
            speak("okay")
            speak("bye sargam have a nice day!!")
            sys.exit()

        
        
        speak('Next Command! sargam!')
