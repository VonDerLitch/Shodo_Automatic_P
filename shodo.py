import subprocess
import os
import time

#Starta o shodo e mata ele
def startShodo():
    os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
    time.sleep(15)
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
