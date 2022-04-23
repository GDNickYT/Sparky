import speech_recognition as sr
import time
import webbrowser
r = sr.Recognizer()
print("Sparky")
print("Running version 1.1.0-alpha")
with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source,duration=1.9)
        print("listening")
        audio = r.listen(source,timeout=3.5)
        data = ''
        try:
            data = r.recognize_google(audio)
            print(data)
            if data == "hello" or data == "hi" or data == "greetings":
                print("You said: " + data)
                print("Hello!")
                print("Press ENTER to continue.")
                input()
            elif data == "what's your name" or data == "what is your name":
                print("You said: " + data)
                print("My name is Sparky! Nice to meet you!")
                print("Press ENTER to continue.")
                input()
            elif data == "open Google":
                webbrowser.open("www.google.com", new=0, autoraise=True)
                print("Press ENTER to continue.")
                input()
            elif data == "open GitHub":
                webbrowser.open("www.github.com", new=0, autoraise=True)
                print("Press ENTER to continue.")
                input()
            elif data == "open YouTube":
                webbrowser.open("www.youtube.com", new=0, autoraise=True)
                print("Press ENTER to continue.")
                input()
            elif data == "open SoundCloud":
                webbrowser.open("www.soundcloud.com", new=0, autoraise=True)
                print("Press ENTER to continue.")
                input()
            elif data == "info" or data == "data":
                print("Sparky")
                print("Running version 1.1.0-alpha")
                print("Press ENTER to continue.")
                input()
            else:
                print("Sorry,I dont know how to reply to that.")
                print("Press ENTER to continue")
                input()
        except sr.UnknownValueError:
            print("Sorry,I didn't seem to get what you said.")
            print("Detailed info:Error Code - 001")
            input()
        except sr.RequestError as e:
            print("Request Error")
            print("Detailed info:Error Code - 002")
            input()
