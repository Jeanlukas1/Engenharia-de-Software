<<<<<<< HEAD
# Contar Linhas e Palavras
#  - Escreva um programa que leia o conteúdo de um arquivo `texto.txt`.
#  - Conte quantas linhas e palavras o arquivo possui e exiba esses valores no console.

with open("texto.txt", "w") as arquivo:
    arquivo.write("ola mundo \n")
    arquivo.write("Prazer em conhecelhos")
    
with open("texto.txt", "r") as arquivo:
    ler = arquivo.read()
    print(f"conteudo do arquivo: {ler}")
    palavra = ler.split()
    numero_palavras = len(palavra)
    linha = ler.splitlines()
    numero_linhas = len(linha)
    print(f"O texto tem {numero_linhas} linhas")
=======
# Contar Linhas e Palavras
#  - Escreva um programa que leia o conteúdo de um arquivo `texto.txt`.
#  - Conte quantas linhas e palavras o arquivo possui e exiba esses valores no console.

with open("texto.txt", "w") as arquivo:
    arquivo.write("ola mundo \n")
    arquivo.write("Prazer em conhecelhos")
    
with open("texto.txt", "r") as arquivo:
    ler = arquivo.read()
    print(f"conteudo do arquivo: {ler}")
    palavra = ler.split()
    numero_palavras = len(palavra)
    linha = ler.splitlines()
    numero_linhas = len(linha)
    print(f"O texto tem {numero_linhas} linhas")
>>>>>>> cc6279fd9b0c9ec82fb35247dd6445c0e80eca8b
    print(f"O texto tem {numero_palavras} palavras") 