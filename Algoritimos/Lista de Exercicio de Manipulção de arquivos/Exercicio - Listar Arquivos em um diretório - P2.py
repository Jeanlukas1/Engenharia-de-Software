#  - Escreva um programa que liste todos os arquivos e diretórios de um determinado diretório 
# (dica: use `os.listdir()`). 
#    - Peça ao usuário para informar o caminho do diretório desejado.


import os

entrada = input("Informe o caminho do diretório desejado: ")

texto  = os.listdir(entrada)

print("Esses são todos os arquivos presentes no diretorio informado", texto)