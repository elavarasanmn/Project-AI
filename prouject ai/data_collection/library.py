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

def lib():
 speak("ask any questions")
 print("RULE 1 ==> wh type question accepted")
 print("RULE 2 ==> if you want details ask detail about")
 while True:
    
    recognized_text = recognize_speech()
    print("website:", recognized_text)
    if "details" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("details","")
                        results=wikipedia.summary(recognized_text,sentences=10)
                        speak("Details about")
                        print(results)
                        speak(results)
                        
    elif "what is" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("what is","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "why" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("why","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "when" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("when","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "where" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("where","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "which" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("which","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "who" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("who","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "whom" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("whom","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "whose" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("whose","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "how" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("How","")
                        results=wikipedia.summary(recognized_text,sentences=5)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "explain briefly" in recognized_text:
                        speak("searching in")
                        recognized_text=recognized_text.replace("How","")
                        results=wikipedia.summary(recognized_text,sentences=20)
                        speak("Details about")
                        print(results)
                        speak(results)
    elif "exit" in recognized_text:
            speak("exit from the library model")
            break
    else:
            speak("try again")