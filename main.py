from sistray import *
from sys import exit
from tkinter import messagebox

import win32api
import win32event
import winerror

mutex_name = "REIDELAS"

# Tenta criar uma instância de mutex exclusiva
mutex = win32event.CreateMutex(None, 1, mutex_name)

# Verifica se o mutex já está em execução
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    messagebox.showinfo("AVISO", "O programa já está aberto, verifique o 'systray', icones ocultos do windows no canto inferior direito. .")
    print("O programa já está em Execução.")
    sysTrayIcon.shutdown()
    exit(0)

# evento de repetição com janela e teste de execução
while True:
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
