import speech_recognition as sr 
import pyttsx3
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"you said : {text}")
            return text.lower()
        except sr.UnknownValueError:
            print(f"sorry, i didn't catch your voice.")
            return ""
        except sr.RequestError:
            print("sorry,my speech service is down.")
            return ""    
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait
def main():
    speak("hello,how can i help you?")
    while True:
        query = listen()
        if "hello" in query:
            speak("hii there")
        elif "time" in query:
            import datetime
            now =datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {now}")
        elif "exit" in query:
            speak("bye bye")
            break
        else:
            speak("sorry i didn't understand that ")
if __name__ =="__main__":
    main()