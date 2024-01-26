import os
import subprocess
import time
import psutil
from tkinter import messagebox

def startShodo():
    # Verificar se o arquivo shodo.exe está presente
    if not os.path.exists("shodo.exe"):
        print("Arquivo shodo.exe não encontrado. Encerrando a aplicação.")
        messagebox.showinfo("Erro", "Arquivo Shodo.exe não encontrado,entre em contato com a equipe de suporte chamados@andrademaia.com")
        print("O programa já está em Execução.")
        # Aqui você pode adicionar código para encerrar a aplicação, como sys.exit() ou raise SystemExit
        return
    
    # Se o arquivo shodo.exe estiver presente, proceda com o restante do código
    for proc in psutil.process_iter():
        if "shodo.exe" in proc.name():
            proc.kill()
        if "javaw.exe" in proc.name():
            proc.kill()
        if "jusched.exe" in proc.name():
            proc.kill()

    os.startfile("shodo.exe")
    time.sleep(20)

    # Verifica novamente os processos e encerra, se necessário
    for proc in psutil.process_iter():
        if "shodo.exe" in proc.name():
            proc.kill()
        if "javaw.exe" in proc.name():
            proc.kill()
