Shodô Automatic 1.1

#Adicionado interface gráfica simples

#Adicionado tempo de execução Shodô 25s

#Adcionado Tutorial De como utilizar, direcionando para Marinet/Drive

#Adicionado mensagem ao executar Shodô 2x

#Adicionado botão de ocupado e disponivel

#Icone adicionado

#Imagem de fundo redimensionada 

#BugFix:Ao sair do programa mensagem de erro

#BugFix:Ao clicar executar shodô pela 2x mensagem de erro

#BugFix:Ao clicar executar shodô, interface não respondia

# Retirado a Task: subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
                   subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
--------------------- Para aumento de desempenho da ferramenta ------------

#BugFix:Ferramenta demorava para executar, foi aumentado o tempo de resposta

#Trocado "ocupado" por "na fila"
******Importante ressaltar  que o DEF "task" foi retirado da execução do programa mas ainda e necessário a utilização do arquivo no programa pois não foi alterado as linhas de código, tendo em vista resolver o problema de imediato.  O "na fila" não irá aparecer pois executará o programa de imediato mesmo que o Shodo esteja em execução pois a "task" verificava se o shodo estava aberto, e a retirada dele elimina essa etapa.*****
