import os
import subprocess
import pyttsx3
from main import *
import pyautogui
import wmi
import cv2

engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate', 140.5)  
engine.setProperty('volume', 30) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def restart_windows():
    os.system("shutdown /r /f /t 0")
def power_off_windows():
    os.system("shutdown /s /f /t 0")
def open_this_pc():
    subprocess.run(["explorer", "/select,", "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"])
def open_start_menu():
    pyautogui.hotkey('win')
def open_windows_settings():
    subprocess.run("start ms-settings:", shell=True)
def enable_bluetooth():
    c = wmi.WMI()
    for interface in c.Win32_PnPEntity():
        if "Bluetooth" in interface.Caption:
            interface.Enable()
def open_bluetooth_settings():
    subprocess.run("start ms-settings:bluetooth", shell=True)
def disable_bluetooth():
    c = wmi.WMI()
    for interface in c.Win32_PnPEntity():
        if "Bluetooth" in interface.Caption:
            interface.Disable()
def open_wifi_settings():
    subprocess.run("start ms-availablenetworks:", shell=True)
def open_wireless_cast_settings():
    subprocess.run("start ms-settings-connectabledevices:", shell=True)
def open_projector_settings():
    subprocess.run("start ms-settings-displays:project", shell=True)
def open_camera():
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually built-in)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Camera Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Windows operation:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

def cmdprogram():
 speak("command mode existing")
 while True:
    
    recognized_text = recognize_speech()
    print("Application:", recognized_text)

    if "shutdown" in recognized_text:
        speak("shutdowning")
        power_off_windows()
    elif "restart" in recognized_text:
        speak("restarting")
        restart_windows()
    elif "this PC" in recognized_text:
        speak("this pc is opening")
        open_this_pc()
    elif "open start" in recognized_text:
        speak("opening start menu")
        open_start_menu()
    elif "open settings" in recognized_text:
        speak("opening setting")
        open_windows_settings()
    elif "turn on Bluetooth" in recognized_text:
        speak("turn on Bluetooth")
        enable_bluetooth()
    elif "turn off Bluetooth" in recognized_text:
        speak("turn off Bluetooth")
        disable_bluetooth()
    elif "open Bluetooth settings" in recognized_text:
        speak("open Bluetooth settings")
        open_bluetooth_settings()
    elif "open Wi-Fi settings" in recognized_text:
        speak("open wifi settings")
        open_wifi_settings()
    elif "open cast settings" in recognized_text:
        speak("open wireless cast settings")
        open_wireless_cast_settings()
    elif "open projector settings" in recognized_text:
        speak("open proujector settings")
        open_projector_settings()
    elif "open camera" in recognized_text:
        speak("opening web camera")
        open_camera()
    elif "exit" in recognized_text:
        speak("exit from the system model")
        break
    else:
        speak("try again ")