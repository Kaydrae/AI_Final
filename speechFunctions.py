import re
import urllib
import webbrowser
from PyQt5.QtGui import QPixmap

from time import sleep
from urllib.request import urlopen
import os

import requests
import soup as soup
import vlc
from jsonpickle import json
from pyowm import OWM
from wikipedia import wikipedia

import speech
from bs4 import BeautifulSoup as soup
from datetime import date, datetime
from pytube import YouTube
import time

s = speech.speech
today = date.today()


class speechFunctions(): # Functions that will execute from what the user is saying.
    def openWebpage(self, command):
        reg_ex = re.search('open (.+)', command) # Search the command for any website after open
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            s.AIResponse('The website you have requested has been opened for you Sir.')
        else:
            pass

    def jokes(self, speak):# Grab a joke from this joke website
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"})
        if res.status_code == requests.codes.ok:

            if speak:# Check to see if the AI is requred to speak
                s.AIResponse(str(res.json()['joke']))
            else:
                self.jokes_text.setPlainText(str(res.json()['joke']))

        else:

            if speak:
                s.AIResponse('oops!I ran out of jokes')
            else:
                self.jokes_text.setPlainText("oops!I ran out of jokes")

    def googleNews(self, speak): # Grab headlines from google news
        try:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item", limit=5)
            # Print news title
            for news in news_list:
                if speak: # Check if required to speak
                    s.AIResponse(news.title.text)
                else:
                    self.news_txt.appendPlainText(news.title.text)
        except Exception as e:
            print(e)

    def weather(self, speak): # Grab current weather from Open weather map
        city = 'Phoenix'
        owm = OWM(API_key='9cc0d740da5a0b79f4075ea569b15cd8')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        k = w.get_status()
        x = w.get_temperature(unit='fahrenheit')

        if speak: # Check if required to speak
            s.AIResponse(
                'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree fahrenheit' % (
                    city, k, x['temp_max'], x['temp_min']))
        else:
            self.weather_text.setPlainText(
                'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree fahrenheit' % (
                    city, k, x['temp_max'], x['temp_min']))

    def time(self):# Get current time
        now = datetime.now()
        s.AIResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))

    def launch(self, command):# Launch a application that is on the computer. Can only get working with Mac OS for now
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname.title() + ".app"
            os.system("open file:///System/Applications/" + appname1)
            s.AIResponse('I have launched the desired application')

    def playSong(self):# Downloads and plays a song from youtube, Will play the song till the song is over
        s.AIResponse('What song shall I play Sir?')
        mysong = speech.speech.myCommand(self) # Listens for long name
        if mysong:
            flag = 0
            url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+') # Creates URL from command function
            r = requests.get(url)
            page = r.text
            soup1 = soup(page, "html.parser")
            url_list = []
            for vid in soup1.findAll('a', attrs={'class': 'yt-uix-tile-link'}):
                if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                    flag = 1
                    final_url = 'https://www.youtube.com' + vid['href']
                    url_list.append(final_url)
                    url = url_list[0]# Grabs the first video URL

            print("downloading your music from youtube")
            s.AIResponse('downloading your music from youtube')
            YouTube(url).streams.filter(subtype='mp4').first().download() #Downloads it
            path = YouTube(url).title # Make the path the name
            s.AIResponse('download complete, now playing')
            print("download complete, now playing")
            player = vlc.MediaPlayer(path + ".mp4")
            player.play() # Plays the song with vlc
            sleep(5)  # delay to let VLC open
            while player.is_playing():
                sleep(1) # Let the song play though
            if flag == 0:
                s.AIResponse('I have not found anything in Youtube ')
                print("I have not found anything in Youtube")

    def changeWallpaper(self):# Change the wallpaper to the "Desktop" (the background of the personal assistant)

        api_key = 'DphBLmcEqXGTCgF3q2UiP6kfR2z40fLfRs4F_Imqq7E'
        url = 'https://api.unsplash.com/photos/random?client_id=' + api_key  # Picture from unspalsh.com

        r = requests.get(url, params={"orientation": "landscape"})# Want only landscape pictures
        #print(r)
        json_string = r.text

        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        #print(photo)
        image = urllib.request.urlretrieve(photo)  # Save to temp location
        #print(image[0])
        image_path = image[0]
        self.wallpaper.setPixmap(QPixmap(image_path))# Set wallpaper
        s.AIResponse('wallpaper changed successfully')

    def wikiSearch(self, command):
        reg_ex = re.search('tell me about (.*)', command)# Get the user is trying to search after the keywords
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                wikiResponse = wikipedia.page(topic)
                s.AIResponse(str(wikiResponse.content[:500].encode('utf-8')))
        except Exception as e:
            print(e)

    def agenda(self, speak):# Check the task file for task for the current day
        try:
            file1 = open("mytasks.txt", "r")# Read the file

            line = file1.readlines()
            for lines in line:

                splitTest = lines.split("+")
                # print(splitTest)
                date = splitTest[0]
                time = splitTest[1]
                event = splitTest[2]
                if date == str(today): # Check if the date is equal to the same

                    if speak:# Check if aloud to speck
                        s.AIResponse(time + " " + event)
                    else:
                        self.todaysEvents_text.appendPlainText(time + " " + event)

            file1.close()
        except Exception as e:
            print(e)

    def help(self, speak):# Help section
        if speak:
            s.AIResponse("1. Open xyz.com : replace xyz with any website name \n "
                         "2. Current weather : Tells you the current condition and temperature \n "
                         "3. Play me a song : Plays song in your VLC media player \n "
                         "4. Change wallpaper : Change desktop wallpaper \n"
                         "5. News for today : reads top news of today \n "
                         "6. Time : Current system time \n "
                         "7.Tell me about xyz : tells you about xyz \n "
                         "8.Launch xyz : replace xyz with an application \n "
                         "9.What is on my agenda\n")
        else:
            self.help_text.setPlainText("1. Open xyz.com : replace xyz with any website name \n "
                                        "2. Current weather : Tells you the current condition and temperature \n "
                                        "3. Play me a video : Plays song in your VLC media player \n "
                                        "4. Change wallpaper : Change desktop wallpaper \n"
                                        "5. News for today : reads top news of today \n "
                                        "6. Time : Current system time \n "
                                        "7.Tell me about xyz : tells you about xyz \n "
                                        "8.Launch xyz : replace xyz with an application \n "
                                        "9.What is on my agenda\n")
