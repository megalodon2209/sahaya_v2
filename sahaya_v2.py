import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import wikipedia
import pyttsx3
import smtplib
import pyautogui
import psutil
import pyjokes
import wolframalpha


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 200)
engine.runAndWait()
speech = sr.Recognizer()


greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
google_searches_dict = {'what': 'what', 'which': 'which', 'when': 'when', 'where': 'where', 'search': 'search',
                        'who': 'who', 'whom': 'whom', 'whose': 'whose', 'why': 'why', 'whether': 'whether'}
social_media_dict = {'facebook': 'https://www.facebook.com/', 'instagram': 'https://www.instagram.com/',
                     'twitter': 'https://twitter.com/explore', ' whatsapp': 'https://www.whatsapp.com/'}
youtube_search_dict = {'play': 'play'}
youtube_song_dict = {'gane': 'gane', 'song': 'song'}

mp3_thankyou_list =['MP3\welcome.mp3']
mp3_listening_problem_list = ['MP3\pardon.mp3', 'MP3\sorry.mp3']
mp3_struggling_list = ['MP3\samaj.mp3', 'MP3\struggle.mp3']
mp3_bye = ['MP3\goodb.mp3', 'MP3\ciao.mp3',]
mp3_google_search = ['MP3\here.mp3', 'MP3\search.mp3']
mp3_greeting_list = ['MP3\hope.mp3', 'MP3\how.mp3']
mp3_open_launch_list = ['MP3\open.mp3', 'MP3\launch.mp3']

error_occurrence = 0

def is_valid_google_search(phrase):
    if google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]:
        return True

def is_valid_youtube_search(phrase):
    if youtube_search_dict.get(phrase.split(' ')[0] == phrase.split(' ')[0]):
        return True

def is_valid_youtube_song(phrase):
    if youtube_song_dict.get(phrase.split(' ')[0] == phrase.split(' ')[0]):
        return True

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('Listening...')

    global error_occurrence

    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:

        if error_occurrence==0:
            play_sound(mp3_listening_problem_list)
            error_occurrence+=1
        elif error_occurrence==1:
            play_sound(mp3_struggling_list)
            error_occurrence+=1

    except sr.RequestError as e:
        print('Network error')
    except sr.WaitTimeoutError:

        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        # 'Hello edith'
        try:

            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except IndexError:
            pass

    return False
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("luciferpro36@gmail.com", 'atharvabagul')
    server.sendmail('luciferpro36@gmail.com', "archiesify@gmail.com", content)
    server.close()
    pyttsx3.speak('Email sent!')

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\HP\Desktop\Friday\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    pyttsx3.speak('CPU percentage is at' + usage)
    battery = psutil.sensors_battery()
    pyttsx3.speak("Battery percentage is at")
    pyttsx3.speak(battery.percent)

def jokes():
    pyttsx3.speak(pyjokes.get_joke())

if __name__ == '__main__':

    playsound('MP3\sahaya.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting...')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            print('In open...')
            play_sound(mp3_open_launch_list)
            if (is_valid_note(social_media_dict, voice_note)):
                # Launch Facebook
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\{}'.format(voice_note.replace('open ', '').replace('launch ', '')))
                print('explorer C:\\{}'.format(voice_note.replace('open ', '').replace('launch ', '')))
            continue
        elif is_valid_google_search(voice_note):
            print("searching...")
            play_sound(mp3_google_search)
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            continue
        elif 'thanks sahaya' in voice_note or'thanks'in voice_note or 'thankyou' in voice_note or 'thankyou sahaya' in voice_note:
            print('Thanks boss...')
            play_sound(mp3_thankyou_list)
            continue
        elif 'wikipedia' in voice_note:
            pyttsx3.speak("Searching...")
            query = voice_note.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            pyttsx3.speak(result)
            continue
        elif 'send email' in voice_note:
            try:
                    pyttsx3.speak('What should i say?')
                    content = voice_note()
                    to = 'luciferpro36@gmail.com'
                    pyttsx3.speak(content)

            except Exception as e:
                print(e)
                pyttsx3.speak('sorry sire! i am unable to send email at the moment please try again latter')

            continue
        elif 'restart' in voice_note or 'restart system' in voice_note:
            os.system("shutdown /r /t 1")
            continue
        elif 'shutdown' in voice_note or 'shutdown system' in voice_note:
            os.system("shutdown /s /t 1")
            continue
        elif 'music sahaya' in voice_note or 'music' in voice_note:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

            pyttsx3.speak('Okay sire here is your music! Enjoy!')
            continue
        elif 'make a note sahaya'in voice_note or 'make a note' in voice_note:
            pyttsx3.speak("What should it say ?")
            data = read_voice_cmd()
            pyttsx3.speak("confirming what you said , you said : "+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            continue
        elif 'browse notes' in voice_note:
            remember = open('data.txt', 'r')
            pyttsx3.speak("yes sire! there are a few.:" +remember.read())
            continue
        elif 'calculate' in voice_note.lower():
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client('7JJ7JV-5TUPXPPXT6')
            index = voice_note.lower().split().index('calculate')
            query = voice_note.split()[index + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(answer)
            pyttsx3.speak("The answer is " + answer)
            continue

        elif 'screenshot sahaya' in voice_note or 'screenshot' in voice_note:
            screenshot()
            pyttsx3.speak("Screenshot captured!")
            continue
        elif 'computer statistics sahaya' in voice_note or 'computer diagnostics':
            cpu()
            continue
        elif 'tell me a joke sahaya' in voice_note or 'joke' in voice_note:
            jokes()
            continue
        elif 'how are you' in voice_note or 'how are you sahaya' in voice_note:
            stMsgs = ['very good sire!', 'just doing my thing!', 'I am good and full of energy!']
            pyttsx3.speak(random.choice(stMsgs))
            continue
        elif 'define yourself' in voice_note or 'define yourself sahaya' in voice_note:
            pyttsx3.speak("I am friday , your personal assistant, a miracle developed in python! I am here to make your life easier. you can command me to perform various tasks")
            continue

        elif 'sahaya name your your developer' in voice_note:
            pyttsx3.speak("I was created or developed by my god Master Atharva Bagul")
            continue
        elif 'youtube' in voice_note or 'youtube sahaya' in voice_note:
            pyttsx3.speak("Opening youtube")
            webbrowser.open('https://www.youtube.com/search?q={}'.format(voice_note))
            continue
        elif 'song sahaya' in voice_note or 'song' in voice_note:
            pyttsx3.speak("Opening youtube music...enjoy")
            webbrowser.open('https://music.youtube.com/search?q={}'.format(voice_note))
            continue
        elif 'jai hind sahaya'in voice_note or 'jai maharashtra sahaya' in voice_note or 'jai hind dosto' in voice_note:
            pyttsx3.speak("jai hind , jai maharashtra")
            continue
        elif 'chrome sahaya' in voice_note or 'google chrome' in voice_note:
            pyttsx3.speak("opening chrome")
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            continue
        elif 'word sahaya' in voice_note or 'msword' in voice_note:
            pyttsx3.speak("opening msword")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk')
            continue
        elif 'powerpoint sahaya' in voice_note or 'mspowerpoint' in voice_note:
            pyttsx3.speak("opening mspowerpoint")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk')
            continue
        elif 'excel sahaya' in voice_note or 'msexcel' in voice_note:
            pyttsx3.speak("opening MS excel")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk')
            continue
        elif 'Access sahaya' in voice_note or 'msAccess' in voice_note:
            pyttsx3.speak("opening MS excel")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Access 2007.lnk')
            continue
        elif 'bye sahaya' in voice_note or 'goodbye sahaya' in voice_note or 'exit sahaya'in voice_note or 'jata' in voice_note:
            print('Good bye...')
            play_sound(mp3_bye) or pyttsx3.speak("Udya Bhhetu")
            exit()

