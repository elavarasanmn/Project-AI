import webbrowser
from main import *

recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate', 140.5)  
engine.setProperty('volume', 30) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def recognize_speech():
    with sr.Microphone() as source:
        print("website name:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

def website():
 speak("what website would you like to open")
 while True:
    
    recognized_text = recognize_speech()
    print("website:", recognized_text)

    if "open WhatsApp" in recognized_text:
       speak("opening")
       url = "https://web.whatsapp.com/"
       webbrowser.open(url)
    elif "open Google" in recognized_text:
       speak("opening google")
       url="https://www.google.com/"
       webbrowser.open(url)
    elif "open YouTube" in recognized_text:
       speak("opening google")
       url="https://www.youtube.com/"
       webbrowser.open(url)
    elif "open Facebook" in recognized_text:
       speak("opening google")
       url="https://www.facebook.com/"
       webbrowser.open(url)
    elif "open FB" in recognized_text:
       speak("opening google")
       url="https://www.facebook.com/"
       webbrowser.open(url)
    elif "open Instagram" in recognized_text:
       speak("opening google")
       url="https://www.instagram.com//"
       webbrowser.open(url)
    elif "open insta" in recognized_text:
       speak("opening google")
       url="https://www.instagram.com//"
       webbrowser.open(url)
    elif "open office" in recognized_text:
       speak("opening google")
       url="https://www.office.com/"
       webbrowser.open(url)
    elif "open Microsoft office" in recognized_text:
       speak("opening google")
       url="https://www.office.com/"
       webbrowser.open(url)
    elif "open open AI" in recognized_text:
       speak("opening google")
       url="https://openai.com/"
       webbrowser.open(url)
    elif "open bing" in recognized_text:
       speak("opening google")
       url="https://www.bing.com/"
       webbrowser.open(url)
    elif "open Gmail" in recognized_text:
       speak("opening google")
       url="https://mail.google.com/"
       webbrowser.open(url)
    elif "open Microsoft" in recognized_text:
       speak("opening google")
       url="https://account.microsoft.com/"
       webbrowser.open(url)
    elif "open Flipkart" in recognized_text:
       speak("opening google")
       url="https://www.flipkart.com/"
       webbrowser.open(url)