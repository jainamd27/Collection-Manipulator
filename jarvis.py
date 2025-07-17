import datetime
import google.genai
import pyttsx3
import speech_recognition as sr
import google
import os
import keyboard
import time
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
voice = engine.setProperty('voice', voices[0].id)
client = google.genai.Client(api_key='AIzaSyAAQB7cXM63W2KV7Xz7maEpBJAWm4Y4b6Q')

def Speak(words):
    engine.say(words)
    print(words)
    engine.runAndWait()

def greetings():
    c_time = datetime.datetime.now().hour
    print(c_time)
    if 0 <= c_time and c_time < 12:
        Speak("Good Morning, sir")
    elif 12 <= c_time and c_time < 16:
        Speak("Good Afternoon, sir")
    elif 16 <= c_time and c_time < 22:
        Speak("Good Evening, sir")
    else:
        Speak("Good Night, sir, it's too late, you need to take a rest now")

def brain(query):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )

    Speak(response.text)

def takeCommand():
    Speak("Listening...")
    r = sr.Recognizer()
    r.energy_threshold = 2500
    r.pause_threshold = 1

    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            Speak("Recognizing...")
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query

        except Exception as e:
            print("Recognition failed, please say that again!!")
            query = input("Please enter your command by typing: ")
            if query:
                return query
            else:
                return "None"

def taskExecution(query):
    if "play" and "music" in query:
        os.startfile("C:\\Users\\jaina\\AppData\\Roaming\\Spotify\\Spotify.exe")
        Speak("Which song do you want to play?")
        s_name = takeCommand()
        keyboard.press('ctrl')
        keyboard.press('k')
        time.sleep(3)
        keyboard.release('ctrl')
        keyboard.release('k')
        keyboard.write(s_name)
        time.sleep(2)
        keyboard.press('shift')
        keyboard.press('enter')
        time.sleep(3)
        keyboard.release('shift')
        keyboard.release('enter')
        time.sleep(1)
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.send('backspace')

    elif "pause" and "music" in query:
        os.startfile("C:\\Users\\jaina\\AppData\\Roaming\\Spotify\\Spotify.exe")
        time.sleep(3)
        keyboard.press('space')

    elif "resume" and "music" in query:
        os.startfile(
            "C:\\Users\\jaina\\AppData\\Roaming\\Spotify\\Spotify.exe")
        time.sleep(3)
        keyboard.press('space')

    elif 'open' and 'YouTube' in query:
        webbrowser.open_new_tab('https://www.youtube.com')

    elif 'open' and 'chat GPT' in query:
        webbrowser.open_new_tab('https://chatgpt.com')
    elif 'send' and 'WhatsApp' in query:
        # Speak("Enter sender's number")
        # s_num = input("Enter sender's number: ")
        Speak("Enter receiver's number")
        r_num = input("Enter receiver's number: ")
        Speak("Please say your message")
        message = takeCommand()
        time.sleep(2)
        pywhatkit.sendwhatmsg_instantly(
            r_num, message)



    else:
        brain(query)

if __name__ == "__main__":
    greetings()
    Speak("I'm Jarvis, your personal AI assistant, please tell me how can I help you?")

    while True:
        query = takeCommand()
        taskExecution(query)
