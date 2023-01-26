from win import window
from shodo import startShodo
from close import startD, closeD
from tkinter import messagebox

import pystray
import PIL.Image

image = PIL.Image.open("iconn.ico")

def on_clicked(icon, item):
    if str(item) == "Abrir":
        event, values = window.read()
    elif str(item) == "Executar Shodo":
        startD()
        startShodo()
        closeD()
    elif str(item) == "Sair":
        exit()


icon = pystray.Icon("Neural", image, menu=pystray.Menu(
    pystray.MenuItem("Abrir", on_clicked),
    pystray.MenuItem("Executar Shodo", on_clicked),
    pystray.MenuItem("Sair", on_clicked)
))

icon.run()
