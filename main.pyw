
from win import window
import os
from sys import exit
from shodo import startShodo
from close import startD, closeD
from task import taskCheck

# evento de repetição

while True:
    event, values = window.read()
    if event == "Executar Shodô":
            startD()
            taskCheck()
            window.hide()
            startShodo()
            window.un_hide()
            closeD()


    if event == "TUTORIAL:Como utilizar":
        os.startfile("https://drive.google.com/file/d/1VM52BT4kTJFkp6rrLkhgiyzkuRm6Iixq/view")

    if event == "Sair":
        exit()

    if event == None:
        exit()
# Qualquer problema ou duvida com o código contactar Principe ignorante(kelvin Silveira), João Pedro.