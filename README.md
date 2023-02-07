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

#Adicionado Sistray (icone na barra de tarefas)
*****To Fix: Botão Sair não funciona, Botão Executar Shodo ???(minha maquina n tem shodo), ao abrir a interface grafica e clicar em sair ele fecha o app, (deveria minimizar, não queremos que o app seja fechado)*****

# COMMIT 0.2 sistray
*Botão executar Shodo do systray funcionando!!
*Botão abrir funcionando, porém app fica travado
*Botão Sair sistray ainda não funciona
*Report: Ao sair duas vezes pelo aplicativo Shodo Automatic, na segunda o Shodo encerra a execução

# COMMIT 0.3 Systray - Working
*Systray funcionando completamente
*Fixed app travado ao re-abrir
*Fixed opção sair não mais disponivel, unica forma de fechar pelo X do app

# Last Commit Main 1.3 Sistray
*Tudo funcionando