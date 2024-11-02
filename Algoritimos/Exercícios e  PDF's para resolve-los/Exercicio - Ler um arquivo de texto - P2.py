# Ler um Arquivo de Texto
#  - Crie um arquivo de texto chamado `mensagem.txt` com algumas linhas de texto.
#  - Escreva um programa que leia todo o conteúdo desse arquivo e o exiba no console

with open("mensagem.txt", "w") as arquivo:
    arquivo.write("Ola mundo, eu sou uma máquina \n")
    arquivo.write("Estou bem e voces como estão \n")
    arquivo.write("Estou me sentindo vivo \n")

with open("mensagem.txt", "r") as arquivo:
    ler = arquivo.read()
    print(ler)