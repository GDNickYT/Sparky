import speech_recognition as sr
import time
import webbrowser
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1.9)
    print("listening")
    audio = r.listen(source,timeout=3)
    data = ''
    try:
        data = r.recognize_google(audio)
        print(data)
        if data == "hello" or data == "hi" or data == "greetings":
            print("You said: " + data)
            print("Hello!")
            input()
        elif data == "what's your name" or data == "what is your name":
            print("You said: " + data)
            print("My name is Sparky! Nice to meet you!")
            input()
        elif data == "open Google":
            webbrowser.open("www.google.com", new=0, autoraise=True)
    except sr.UnknownValueError:
        print("Sorry,I didn't seem to get what you said.")
    except sr.RequestError as e:
        print("Request Error")