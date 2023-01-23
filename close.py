from win import window

# Starta o botão
def startD():
    window['u'].update('Ocupado', button_color='red')
    window.refresh()

# Fecha o botão
def closeD():
    window['u'].update('Disponível', button_color='green')
    window.refresh()