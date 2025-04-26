import speech_recognition as sr 
import os
import win32com.client
import time
import pyttsx3
import webbrowser
import datetime


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "some error sorry from jarvis"
        

def close_app(process_name):
    os.system(f"taskkill /f /im {process_name}")
    
if __name__ == '__main__':
    speaker.Speak("Hello I am jarvis")
    while True:
        print("Listening")
        query =takecommand()
        sites = [["youtube","https://youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    speaker.Speak(f"opening {site[0]} sir...")
                    webbrowser.open(site[1])  

                elif "kAise Ho".lower() in query.lower():
                    speaker.Speak("mai thik hu")
                    pass

                elif "faVourite song".lower() in query.lower():
                    speaker.Speak("your favourite song playing sir..")
                    musicpath = r"C:\Users\91746\Music\Saudebaazi.mp3"
                    os.startfile(musicpath)
                    break

                elif "stop song".lower() in query.lower():
                    process_name = "vlc.exe"
                    
                    close_app(process_name)
                    speaker.Speak("song stoped sir")
                    break

                elif "close browser".lower() in query.lower():
                    process_name = "msedge.exe"
                    close_app(process_name)
                    speaker.speak("broswer closed sir")
                    break

                elif "the time".lower() in query.lower():
                    hour =datetime.datetime.now().strftime("%H")
                    minuts =datetime.datetime.now().strftime("%M")
                    # sec =datetime.datetime.now().strftime("%S")
                    speaker.Speak(f"sir time is {hour} hours and  {minuts} minutes ")
                    break
                elif "open visual studeio".lower() in query.lower():
                    pass
                    





                    

     
    
