from win import window
from shodo import startShodo
from close import startD, closeD

import pystray
import PIL.Image

image = PIL.Image.open("iconn.ico")


def on_clicked(icon, item):
    if str(item) == "Abrir":
        window.un_hide()

    elif str(item) == "Executar Shodo":
        window.un_hide()
        startD()
        window.hide()
        startShodo()
        closeD()

    elif str(item) == "Sair App":
        exit()
    if icon == True:
        icon.stop()


icon = pystray.Icon("Neural", image, menu=pystray.Menu(
    pystray.MenuItem("Abrir", on_clicked),
    pystray.MenuItem("Executar Shodo", on_clicked),
    pystray.MenuItem("Sair App", on_clicked)
))
