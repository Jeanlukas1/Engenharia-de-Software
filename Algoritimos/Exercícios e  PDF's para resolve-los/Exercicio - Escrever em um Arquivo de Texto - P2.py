# Escrever em um Arquivo de Texto
#  - Crie um programa que peça ao usuário para digitar uma frase.
#  - Escreva essa frase em um novo arquivo chamado `frase_usuario.txt`.

with open("frase_usuario.txt", "w") as arquivo:
    frase = input("Digite algo a ser adicionado ao texto: ")
    print(arquivo.write(f"{frase}"))

with open("frase_usuario.txt", "r") as arquivo:
    ler = arquivo.read()
    print(ler) 
