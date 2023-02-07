import subprocess
import os
import time

<<<<<<< HEAD
#Starta o shodo e mata ele
def startShodo():
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
    os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
    time.sleep(25)
=======
# Starta o shodo e mata ele

def startShodo():
    os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
    time.sleep(15)
>>>>>>> 16dac99bb1063cc9432bafc12f84afadc979a66e
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
