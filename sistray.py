from win import window
from libs.sistrayLib import SysTrayIcon
import os
from shodo import startShodo

hover_text = "Shodo Automatic"


def open(sysTrayIcon):
    window.un_hide()


def shodo(sysTrayIcon):
    sysTrayIcon.update("iconn.ico", "EM EXECUÇÃO")

    window.hide()
    startShodo()
    sysTrayIcon.update("icon.ico", "Shodo Automatic")


menu_options = (('Abrir', None, open),
                ('Executar Shodo', None, shodo))

sysTrayIcon = SysTrayIcon("icon.ico", hover_text,
                          menu_options, default_menu_index=0)


sysTrayIcon.start()
