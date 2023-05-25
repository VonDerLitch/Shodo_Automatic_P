from PySimpleGUI import (Window, Button, Text, Image,Column, VSeparator, theme) 

#layout

theme('Black')

layout_esquerda = [
    [Image(filename='logg.png')],
]

layout_direita = [
    [Text('Shodô Automatic ', text_color='OrangeRed', justification='center')],
    [Button('Executar Shodô', size=20)], [Button('TUTORIAL:Como utilizar', size=20)], [Button('Minimizar', size=20)]
]

layout_u = [
    [Button('Disponível', size=22, button_color='green', key='u')]
]

layout_f = [
    [Button('NA FILA', size=22, button_color='red', key='f')]
]

layout = [
    [Column(layout_direita),  VSeparator(), Column(layout_esquerda), layout_u]
]

window = Window(
    'Shodô Automatic 1.3',
    layout=[[layout]],
    font=55,
    icon=r'icon.ico',
    size=(500,220),

)
