import os
from main import *

recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Application name:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

def file():
 speak("what application would you like to open")
 while True:
    
    recognized_text = recognize_speech()
    print("Application:", recognized_text)

    if "vs code" in recognized_text:
        speak("opening")
        vscodepath="C:\\Users\\elava\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vscodepath)
    elif "Adobe Reader" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files (x86)\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
                os.startfile(vscodepath)
    elif "Photoshop" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
                os.startfile(vscodepath)
    elif "brave Browser" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                os.startfile(vscodepath)
    elif "Excel" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(vscodepath)
    elif "PowerPoint" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(vscodepath)
    elif "Outlook" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
                os.startfile(vscodepath)
    elif "Visual Studio" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
                os.startfile(vscodepath)
    elif "Chrome" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(vscodepath)
    elif "Microsoft edge" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(vscodepath)
    elif "Firefox" in recognized_text:
                speak("opening")
                vscodepath="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(vscodepath)
    elif "exit" in recognized_text:
            speak("exit from the application model")
            break
    else:
        speak("it is invalide command,try again")
    