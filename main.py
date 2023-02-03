from sistray import *

# evento de repetição



while True:
    event, values = window.read()
    if event == "Executar Shodô":
        window.hide()
        startShodo()
        window.un_hide()
    if event == "TUTORIAL:Como utilizar":
        os.startfile(
            "https://drive.google.com/file/d/18pTMRX-nY437Gh8R6P6XBUsDsOjTOob6/view")

    if event == "Sair":
        window.hide()

    if event == None:
        sysTrayIcon.shutdown()
        exit()
    
    
# Qualquer problema ou duvida com o código contactar Principe ignorante(kelvin Silveira), João Pedro.
