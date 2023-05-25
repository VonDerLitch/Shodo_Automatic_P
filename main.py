from sistray import *
from sys import exit
from msgbox import check_process

# evento de repetição com janela e teste de execução
while True:
    check_process
    event, values = window.read()
    if event == "Executar Shodô":
        window.hide()
        startShodo()
        window.un_hide()
    if event == "TUTORIAL:Como utilizar":
        os.startfile(
            "https://drive.google.com/file/d/18pTMRX-nY437Gh8R6P6XBUsDsOjTOob6/view")

    if event == "Minimizar":
        window.hide()

    if event == None:
        sysTrayIcon.shutdown()
        exit()
    
# Qualquer problema ou duvida com o código contactar Niflheim Morke(kelvin silveira) ou Kaio.
