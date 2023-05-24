import subprocess
import os
import time

#Starta o shodo e mata ele
def startShodo():
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
<<<<<<< Updated upstream
    os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
    time.sleep(25)
=======
    subprocess.call("TASKKILL /F /IM jusched.exe", shell=True)
    os.startfile("shodo.exe")
    time.sleep(20)
>>>>>>> Stashed changes
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
