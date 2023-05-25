import psutil
import sys
import tkinter as tk
from tkinter import messagebox

#Verifica se o programa está em execução
def check_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

if check_process("Shodo Automatic.exe"):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("AVISO programa já está em execução", "Programa já está aberto, verifique a aba 'systray', no canto inferior direito nos icones ocultos.")
    sys.exit()
