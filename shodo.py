import subprocess
import os
import time


# Starta o shodo e mata ele

def startShodo():
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
    subprocess.call("TASKKILL /F /IM jusched.exe", shell=True)
    os.startfile("shodo.exe")
    time.sleep(20)
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
