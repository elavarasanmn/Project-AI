from tkinter import *
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file='images//2.png')
height = 239
width = 217
x=(root.winfo_screenwidth()//2)-(width//2)
y=(root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
root.overrideredirect(1)

root.wm_attributes('-topmost',True)
root.lift()
root.wm_attributes("-topmost",True)
root.wm_attributes("-disable",True)
root.wm_attributes("-transparentcolor","white")
bg_label = Label(root,image=image,bg='white')
bg_label.place(x=0,y=0)

Progr_label = Label(root,text="Please Wait...",font=('Comic Sans MS',13,'bold'))
Progr_label.place(x=190,y=480)
progress = Progressbar(root, orient=HORIZONTAL,length=360, mode='determinate')
progress.place(x=190,y=480)

def top():
    root.withdraw()
    os.system("python home.py")
    root.destroy()

i=0

def load():
    global i
    if i<=10:
        txt = 'please wait.... '+(str(10*i)+'%')
        Progr_label.config(text=txt)
        Progr_label.after(1000,load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

load()


root.mainloop()