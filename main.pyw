
from win import window
import os
from sys import exit
from shodo import startShodo
from close import startD, closeD
from sistray import icon

# evento de repetição

while True:
    event, values = window.read()
    if event == "Executar Shodô":
        startD()
        window.hide()
        startShodo()
        window.un_hide()
        closeD()

    if event == "TUTORIAL:Como utilizar":
        os.startfile(
            "https://drive.google.com/file/d/18pTMRX-nY437Gh8R6P6XBUsDsOjTOob6/view")

    if event == "Sair":
        window.hide()
        window.refresh()
        icon.run()

    if event == None:
        window.hide()

# Qualquer problema ou duvida com o código contactar Principe ignorante(kelvin Silveira), João Pedro.
