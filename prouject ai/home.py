from tkinter import *
from tkinter.ttk import Progressbar
import os
import subprocess

root = Tk()
image = PhotoImage(file='images//i1.png')
height = 239
width = 217
x=(root.winfo_screenwidth()//2)-(width//2)
y=(root.winfo_screenheight()//2)-(height//2)
x=1315
y=0
root.geometry(f"{width}x{height}+{x}+{y}")
root.overrideredirect(1)

root.wm_attributes('-topmost',True)
root.lift()
root.wm_attributes("-topmost",True)
root.wm_attributes("-disable",True)
root.wm_attributes("-transparentcolor","white")
bg_label = Label(root,image=image,bg='white')
bg_label.place(x=0,y=0)



proc1 = subprocess.Popen(['python','main.py'])
proc2 = subprocess.Popen(['python','mouse.py'])






root.mainloop()
proc1.wait()
proc2.wait()