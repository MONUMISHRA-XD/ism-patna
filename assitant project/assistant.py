import speech_recognition as sr #for listen and understand the word
import pyttsx3 #for text to speak
import pvporcupine #jarvis awake
import pyaudio
import struct
import requests
import os

my_pico_voice_key = "g5uJHfVm3/fO04QAWVb40LVIsAWoF/PUG2kdCbbOTlyS4Q5IWqsNWA=="

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
    engine.runAndWait()

def detect_wake_word():
    porcupine =pvporcupine.create(access_key=my_pico_voice_key,keywords=["jarvis"])
    audio_stream = pyaudio.PyAudio().open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    print("Waiting for wake word...")
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Wake word detected!")
            break

BASE_URL = "https://newsapi.org/v2/top-headlines"
news_api = "a6df0eff75454272956444faf3860992"
def get_news(country="in", category="technology"):
    params = {
        "country": country,
        "category": category,
        "apiKey": news_api
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])

        if not articles:
            speak("Sorry, no news articles found.")
            return

        speak("Here are the latest news headlines.")
        
        for i, article in enumerate(articles[:5], 1):  # Get top 5 news
            news_title = article['title']
            print(f"{i}. {news_title}")
            speak(news_title)

    else:
        speak("Sorry, I couldn't fetch the news.")
        print("Error:", response.status_code, response.text)
# def search_news(query="python"):
#     url = "https://newsapi.org/v2/everything"
#     params = {
#         "q": query,
#         "apiKey": news_api
#     }

#     response = requests.get(url, params=params)
    
#     if response.status_code == 200:
#         news_data = response.json()
#         for article in news_data["articles"][:5]:  # Get top 5 articles
#             print(f"- {article['title']}: {article['url']}")
#     else:
#         print("Error fetching news.")

# search_news("Python")

    
def close_app(process_name):
    os.system(f"taskkill /f /im {process_name}")

def main():
    detect_wake_word()
    speak("hello,how can i help you?")
    sites = [["youtube","https://youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
    for site in sites:
        if f"open{site[0]}".lower() in query.lower():
            speak("opening {site[0]} sir")
    while True:
        query = listen()
        if "hello" in query:
            speak("hii there")
        
        elif "kAise Ho".lower() in query.lower():
            speak("mai thik hu")
        

        elif "faVourite song".lower() in query.lower():
                speak("your favourite song playing sir..")
                musicpath = r"C:\Users\91746\Music\Saudebaazi.mp3"
                os.startfile(musicpath)


        elif "stop song".lower() in query.lower():
                process_name = "vlc.exe"
                close_app(process_name)
                speak("song stoped sir")

        elif "close browser".lower() in query.lower():
            process_name = "msedge.exe"
            close_app(process_name)
            speak("broswer closed sir")   
        elif "open visual studeio".lower() in query.lower():
            pass
        elif "time" in query:
            import datetime
            hour =datetime.datetime.now().strftime("%H")
            minuts =datetime.datetime.now().strftime("%M")
            speak(f"sir time is {hour} hours and  {minuts} minutes ")
        elif "tech news" in  query:
            get_news()
        elif "exit" in query:
            speak("bye bye")
            break
        else:
            speak("sorry i didn't understand that ")

if __name__ =="__main__":
    main()
