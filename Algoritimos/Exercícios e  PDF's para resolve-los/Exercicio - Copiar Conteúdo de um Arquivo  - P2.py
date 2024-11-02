
# Copiar Conteúdo de um Arquivo
#  - Escreva um programa que leia o conteúdo de um arquivo chamado `origem.txt` e o copie
# para um novo arquivo chamado `copia.txt`.

from shutil import copyfile

with open('origem.txt', 'w') as arquivo:
    arquivo.write("ola mundo \n")
    arquivo.write("Prazer em conhecelhos")
    
with open('origem.txt', 'r') as arquivo:
    ler = arquivo.read()
    print(f"conteudo do arquivo: {ler}")

copia = copyfile('origem.txt', 'copia.txt')

print(f"Texto copiado no seu diretório como : {copia}")

