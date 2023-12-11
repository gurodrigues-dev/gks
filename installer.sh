chmod u+x ./gks.py

diretorio_atual=$(pwd)

echo "alias gks='${diretorio_atual}/gks.py'" >> ~/.bashrc

source ~/.bashrc

echo "Instalação concluída. Agora você pode usar o comando 'gks' para executar o script."
