from win import window
from infi.systray import SysTrayIcon
import os
from shodo import startShodo


def automatic():
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
        exit()


hover_text = "Shodo Automatic Demo"


def open(sysTrayIcon):
    window.un_hide()


def shodo(sysTrayIcon):
    window.un_hide()
    window.hide()
    startShodo()


menu_options = (('Abrir', "Da p colocar icone aqui se quiser", open),
                ('Executar Shodo', None, shodo),

                )
sysTrayIcon = SysTrayIcon("iconn.ico", hover_text,
                          menu_options, on_quit=None, default_menu_index=1)
