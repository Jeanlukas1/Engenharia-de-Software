
# Copiar Conteúdo de um Arquivo
#  - Escreva um programa que leia o conteúdo de um arquivo chamado `origem.txt` e o copie
# para um novo arquivo chamado `copia.txt`.

from shutil import copyfile

with open('Lista de Exercicio de Manipulção de arquivos/origem.txt', 'w') as arquivo:
    arquivo.write("ola mundo \n")
    arquivo.write("Prazer em conhecelhos")
    
with open('Lista de Exercicio de Manipulção de arquivos/origem.txt', 'r') as arquivo:
    ler = arquivo.read()
    print(f"conteudo do arquivo: {ler}")

copia = copyfile('Lista de Exercicio de Manipulção de arquivos/origem.txt', 'Lista de Exercicio de Manipulção de arquivos/copia.txt')

print(f"Texto copiado no seu diretório como : {copia}")

