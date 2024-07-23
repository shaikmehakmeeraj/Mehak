import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import wikipedia
import random
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-in')
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand")
            return None
def open_website(website):
    webbrowser.open(website)
def search_wikipedia(query):
    results = wikipedia.search(query)
    if results:
        speak("Here's what I found on Wikipedia:")
        speak(results[0])
    else:
        speak("Sorry, I couldn't find anything on Wikipedia")

def tell_time():
    now = datetime.datetime.now()
    speak("The current time is " + now.strftime("%H:%M:%S"))
def play_music():
    music_dir = "/path/to/music/directory"
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))

def send_email(to, subject, body):
def set_reminder(reminder):
    pass

# Main loop
while True:
    voice_input = get_voice_input()
    if voice_input:
        if "open" in voice_input:
            website = voice_input.split("open ")[1]
            open_website(website)
        elif "search" in voice_input:
            query = voice_input.split("search ")[1]
            search_wikipedia(query)
        elif "time" in voice_input:
            tell_time()
        elif "play music" in voice_input:
            play_music()
        elif "send email" in voice_input:
            to = input("Enter the recipient's email: ")
            subject = input("Enter the subject: ")
            body = input("Enter the body: ")
            send_email(to, subject, body)
        elif "set reminder" in voice_input:
            reminder = input("Enter the reminder: ")
            set_reminder(reminder)
        else:
            speak("Sorry, I didn't understand")
