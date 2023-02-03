from win import window
from libs.sistrayLib import SysTrayIcon
import os
from shodo import startShodo
    
hover_text = "Shodo Automatic Demo"

def open(sysTrayIcon):
    window.un_hide()


def shodo(sysTrayIcon):
    window.hide()
    startShodo()
    


menu_options = (('Abrir', None, open),
                ('Executar Shodo', None, shodo),

                )
sysTrayIcon = SysTrayIcon("iconn.ico", hover_text,
                          menu_options, default_menu_index=1)
                          
sysTrayIcon.start()