# 1. Can greet you
# 2. Can tell you time
# 3. Can tell you wheather report in country
# 4. Can search query in google
# 5. Can browse any website
# 6. Can open and close application.....update path as desktop and try to open all applications from desktop so that code can be dynamically updated
# 7. Can shutdown restart logoff your pc
# 8. Can calculate some problems
# 9. Can search in wikipedia
# 10. Tells you the news
# 11. Tells you a jokes
# 12. Download and plays a video from youtube
# 13. Can search a song in youtube
# 14. Create and delete folders
# 15. play music
# 16. play a video

#Required to Complete
# open startup in windows
# modify the open application system




import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as wb
import os
import sys
import re
import smtplib
import wolframalpha
from weather  import Weather
from selenium import webdriver
import requests
from lxml import html 
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup as soup
import random
import sympy
import shutil

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

google_searches = {'what':'what','why':'why','which':'which','when':'when','what':'what'}

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('22XYLA-GG8APGHKPG')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def valid_google_searches(phrase):
    if(google_searches.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Jannu Sir , your AI personal assistant. I am here to help you sir.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak('Recognizing sir')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak("U said, " + query + '.')
        
    except sr.UnknownValueError:
        # print(e)    
        speak('Sorry sir I do not recieved any input from you')
        speak('please say that again sir')
        query = takeCommand()
    return query
  

if __name__ == "__main__":
    wishMe()
    speak("may I know your name, sir?") 
    name = 'preetham'
    name = takeCommand() 
    speak("Hello, " + name + '.') 
    speak('Thanks for choosing me, sir')
  
    while True:
        
    # if 1:
        query = takeCommand().lower()

        # To stop Jannu

        if "exit" in str(query) or "bye" in str(query) or "sleep" in str(query): 
            speak("Ok bye, "+ name+'.') 
            speak('have a good day.')
            break        
        # tells that what jannu can do

        elif "what can you" in query:
            speak('I Can greet you')
            speak('I Can tell you time')
            speak('I Can tell you wheather report in country')
            speak('I Can search query in google')
            speak('I Can browse any website')
            speak('I Can open and close application')
            speak('I Can shutdown restart logoff your pc')
            speak('I Can calculate some problems')
            speak('I Can search in wikipedia')
            speak('I can Tell you the news')
            speak('I can Tell you a jokes')
            speak('I can Download and plays a video from youtube')
            speak('I Can search a song in youtube')
            speak('I can Create and delete folders')
            speak('I can play music')
            speak('I can play a video')
            continue


        # Search query in google

        elif valid_google_searches(query):
            speak('ok sir.Let me search  your query in google....please hold on')
            speak('yeah got the results sir....')
            print('searching in google....')
            try:
                wb.open('https://www.google.co.in/search?q={}'.format(query))
            except e:
                speak('The request cannot be proceed right now sir!')
            else:
                speak('Requested query has been searched for you sir!')
            continue

        # Search website in browser

        elif 'search' in query:
                reg_ex = re.search('search (.+)', query)
                if reg_ex:
                    domain = reg_ex.group(1)
                    print(domain)
                try:
                    url = 'https://www.' + domain
                    wb.open(url)
                except e:
                    speak('The requested query cannot be proceeded right now sir')
                else:
                    speak('The website you have requested has been opened for you Sir.')
                    continue

                    # searches youtube video in browser

        elif 'search video' in query:
                reg_ex = re.search('play video (.+)', query)
                if reg_ex:
                    domain = reg_ex.group(1)
                    print(domain)
                try:
                    url = 'https://www.youtube.com/results?search_query=' + domain
                    wb.open(url)
                except e:
                    speak('The requested query cannot be proceeded right now sir')
                else:
                    speak('The song you have requested has been opened for you Sir.')
                    continue


        # weather report in current city

        elif 'current weather' in query:
                   reg_ex = re.search('current weather in (.*)', query)
                   if reg_ex:
                     city = reg_ex.group(1)
                     owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                     obs = owm.weather_at_place(city)
                     w = obs.get_weather()
                     k = w.get_status()
                     x = w.get_temperature(unit='celsius')
                     print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
                     speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
                     continue
        
            # describes about jannu

        elif 'describe yourself' in query or 'define yourself' in query: 
            speak('Hello, I am jannu sir. Your personal Assistant. I am here to make your life easier. You can command me to perform  various tasks such as calculating sums or opening applications etcetra')
            continue

            # tells time

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            continue

            # plays music

        elif 'play music' in query:
                reg_ex = re.search('play music (.*)', query)
                if reg_ex:
                    song = reg_ex.group(1)
                    songname = song.replace(" ","")
                    song1 = songname+".mp3"
                    print(song1)
                    path = "C:\\Users\\preet\\Music\\"+ song1+'.'
                try:
                    os.startfile(path)
                except OSError:
                    speak('The song could not be found')
                else:
                    speak('I have played your song sir')
                    continue   
        
                    # plays video

        elif 'play video' in query:
                reg_ex = re.search('play video (.*)', query)
                if reg_ex:
                    song = reg_ex.group(1)
                    songname = song.replace(" ","")
                    song1 = songname+".mp4"
                    print(song1)
                    path = "C:\\Users\\preet\\Videos\\"+ song1+'.'
                try:
                    os.startfile(path)
                except OSError:
                    speak('The song could not be found')
                else:
                    speak('I have played your song sir')
                    continue

            # plays video in VLC

        elif 'download me a video' in query:
                path = 'C:\\Users\\preet\\Downloads\\Video'
                folder = path
                for the_file in os.listdir(folder):
                    file_path = os.path.join(folder, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(e)
                    else:
                        speak('What song shall I play Sir?')

                mysong = takeCommand()
                if mysong:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    response = urllib.request.urlopen(url)
                    html = response.read()
                    soup1 = soup(html,"lxml")
                    url_list = []
                    for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                        if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                            flag = 1
                            final_url = 'https://www.youtube.com' + vid['href']
                            url_list.append(final_url)
                            url = url_list[0]
                            ydl_opts = {}
                            os.chdir(path)
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([url])
                            vlc.play(path)
                if flag == 0:
                                speak('I have not found anything in Youtube ')


        # creates and delete folder on desktop

        elif 'create folder in desktop' in str(query):
                reg_ex = re.search('create folder in desktop(.*)', query)
                if reg_ex:
                    folder = reg_ex.group(1)
                    speak('Sir please tell the name of the folder you want to create')
                    folder = takeCommand()
                    foldername = folder.replace(" ","")
                    print(foldername)
                try:
                    path = "C:\\Users\\preet\\Desktop\\"+ foldername+'.'
                    os.mkdir(path)
                except OSError:
                    speak('Sorry sir I cannot create the folder')
                else:
                    speak("I have created folder with specified name sir")
                    continue

        elif 'delete folder in desktop' in str(query):
                reg_ex = re.search('delete folder in desktop(.*)', query)
                if reg_ex:                    
                    speak('Sir please tell the name of the folder')
                    folder = reg_ex.group(1)
                    folder = takeCommand()
                    foldername = folder.replace(" ","")
                    print(foldername)
                try:
                    path = "C:\\Users\\preet\\Desktop\\"+ foldername+'.'
                    os.rmdir(path)
                except OSError:
                    speak('sorry sir I cannot delete the folder')
                else:
                    speak("I have deleted folder with specified name sir")
                    continue

            # Open applications and closes them

        elif 'launch an app' in query:
                reg_ex = re.search('launch an app(.*)', query)
                if reg_ex:
                    speak('sir please tell the name of the application you want to launch')
                    app = reg_ex.group(1)
                    app = takeCommand()
                    appname = app.replace(" ","")
                    appname1 = appname+".exe"
                    print(appname1)
                    codePath = (" start " + appname1)
                try:
                    os.system(codePath)                    
                except OSError:
                    speak('Windows cannot find desired application')
                else:
                    speak('I have launched the desired application')
                    continue

        elif 'close the app' in query:
                reg_ex = re.search('close the app(.*)', query)
                if reg_ex:
                    speak('sir please tell the name of the application you want to close')
                    app = reg_ex.group(1)
                    app = takeCommand()
                    appname = app.replace(" ","")
                    appname1 = appname+".exe"
                    print(appname1)
                    codePath = (" taskkill -im " + appname1)
                    os.system(codePath)
                    speak('I have closed the desired application')
                    continue

        elif 'open visual studio' in query:
            speak('opening visual studio sir please wait')
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)
            continue

        elif 'close visual studio' in query:
            speak('closing visual studio sir please wait')          
            os.system('taskkill -im devenv.exe')
            continue

        elif 'open notepad plus plus' in query:
            speak('opening notepad plus plus sir please wait')
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)
            continue

        elif 'close notepad plus plus' in query:
            speak('closing notepad plus plus sir please wait')        
            os.system('taskkill -im notepad++.exe')
            continue

        
        elif 'open python' in query:
            speak('opening python sir please wait')
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\python.exe"
            os.startfile(codePath)
            continue

        elif 'close python' in query:
            speak('closing python sir please wait')       
            os.system('taskkill -im python.exe')
            continue

        elif 'open chrome' in query:
            speak('opening chrome sir please wait')
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            continue

        elif 'close chrome' in query:
            speak('closing chrome sir please wait')
            os.system('taskkill -im chrome.exe')
            continue

        
        elif 'open antivirus' in query:
            speak('opening antivirus sir please wait')
            codePath = "C:\\Program Files\\Common Files\\mcafee\\platform\\McUICnt.exe"
            os.startfile(codePath) 
            continue
            
        elif 'close antivirus' in query:
            speak('closing antivirus sir please wait')
            os.system('taskkill -im McUICnt.exe')
            continue
            
        elif 'open Onedrive' in query:
            speak('opening onedrive sir please wait')
            codePath = "C:\\Users\\preet\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"
            os.startfile(codePath)
            continue
            
        elif 'close onedrive' in query:
            speak('closing onedrive sir please wait')           
            os.system('taskkill -im oneDrive.exe')
            continue

        elif 'open powershell' in query:
            speak('opening powershell sir please wait')
            codePath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"  
            os.startfile(codePath) 
            continue

        elif 'close powershell' in query:
            speak('closing powershell sir please wait')
            os.system('taskkill -im powershell.exe')
            continue
            

        elif 'open C plus plus' in query:
            speak('opening c plus plus sir please wait')
            codePath = "C:\\TURBOC3\\Turbo C++\\"
            os.startfile(codePath) 
            continue

        elif 'close C plus plus' in query:
            speak('closing c plus plus sir please wait')           
            os.system('taskkill -im Turbo C++')
            continue

        elif 'open IDM' in query:
            speak('opening internet download manager sir please wait')
            codePath = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
            os.startfile(codePath) 
            continue

        elif 'close idm' in query:
            speak('closing internet download manager sir please wait')            
            os.system('taskkill -im IDMan.exe')
            continue

        elif 'open paint' in query:
            speak('opening paint sir please wait')
            codePath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(codePath)
            continue
            
        elif 'close paint' in query:
            speak('closing paint sir please wait')          
            os.system('taskkill -im mspaint.exe')
            continue

        elif 'open Netbeans' in query:
            speak('opening netbeans sir please wait')
            codePath = "C:\\Program Files\\NetBeans 8.1\\bin\\netbeans.exe" 
            os.startfile(codePath)
            continue

        elif 'close Netbeans' in query:
            speak('closing netbeans sir please wait')           
            os.system('taskkill -im netbeans.exe')
            continue

            # shutdown restart logoff your PC

        elif 'shutdown' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('shutting down your computer please wait')
            os.system('shutdown -s')

        elif 'restart' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('Restarting  your computer please wait')
            os.system('shutdown -r')

        elif 'logoff' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('loggingoff your computer please wait')
            os.system('shutdown -l')

            # tells news

        elif 'news for today' in query:
                try:
                    news_url="https://news.google.com/news/rss"
                    Client=urlopen(news_url)
                    xml_page=Client.read()
                    Client.close()
                    soup_page=soup(xml_page,"xml")
                    news_list=soup_page.findAll("item")
                    for news in news_list[:15]:
                        print(news.title.text.encode('utf-8'))
                        speak(news.title.text.encode('utf-8'))
                except Exception as e:
                    print(e)

                    # tells joke

        elif 'joke' in query:
                res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"})
                if res.status_code == requests.codes.ok:
                    print(str(res.json()['joke']))
                    speak(str(res.json()['joke']))
                else:
                    speak('oops!I ran out of jokes')
                    continue
            # searches in wikipedia and calculate the sums using wolfram alpha

        else:
           query = query
           speak('Searching...')
           try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    print(results)
                    speak(results)  
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    print(results)
                    speak(results) 
                    
           except:
                wb.open('www.google.com')


  
    
  
 
           


    
