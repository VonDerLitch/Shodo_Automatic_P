import os
import sys
import tempfile


lock_file = os.path.join(tempfile.gettempdir(), "program.lock")

# Verificar se o arquivo de bloqueio já existe
if os.path.isfile(lock_file):
    print("O programa já está em execução.")
    sys.exit()

# Criar o arquivo de bloqueio
with open(lock_file, "w") as f:
    f.write("")

# Resto do código do programa...

# Remover o arquivo de bloqueio ao encerrar o programa
os.remove(lock_file)