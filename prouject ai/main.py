import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from data_collection import file_operation
from data_collection import systemoper
from data_collection import web
from data_collection import library

engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate', 140.5)  
engine.setProperty('volume', 30) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def toDaysDate():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        engine.say("Good morning sir!")
    elif hour >= 12 and hour<16:
        engine.say("Good afternoon sir!")
    elif hour >=16 and hour<18:
        engine.say("good evening sir!")
    else:
        engine.say("Good night")
    text_to_speak = "i am master Elavarasan Artificial Intelligence"
    #speak("hi my self is Helen") 
    speak(text_to_speak)
    speak("welcome to the ai world")
recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("I AM READY TO HELP")
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)
def recognize_speech1():
    with sr.Microphone() as source:
        print("Search Datas:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

if __name__ == "__main__":
    toDaysDate()
        
    while True:
            
                recognized_text = recognize_speech1()
                print("You said:", recognized_text)
                if "hello" in recognized_text:
                        speak("hi how are you")
                elif "what about you" in recognized_text:
                        speak("I am fine") 
                elif "I am fine" in recognized_text:
                        speak("what about you")  
                elif "tell about you" in recognized_text:
                        speak("i am a voice assistent,i solve your questions and i can help you")
                        speak("i am developed by Elavarasan A")
                        speak("i developed for help bliend people and future purpos") 
                elif "about yourself" in recognized_text:
                        speak("i am a voice assistent,i solve your questions and i can help you")
                        speak("i am developed by Elavarasan A")
                        speak("i developed for help bliend people and future purpos") 
                elif "thank you" in recognized_text:
                        speak("you are welcome")   
                elif "exit" in recognized_text:
                        speak("Thank you for using me")
                        break
                elif "open applications" in recognized_text:
                        file_operation.file()
                elif "change system mode" in recognized_text:
                        systemoper.cmdprogram()
                elif "open website" in recognized_text:
                        web.website()
                elif "open library" in recognized_text:
                      library.lib()
                
                      
                else:
                        speak("try again")
        
             