import subprocess

proc1 = subprocess.Popen(['python','main.py'])
proc2 = subprocess.Popen(['python','mouse.py'])

proc1.wait()
proc2.wait()