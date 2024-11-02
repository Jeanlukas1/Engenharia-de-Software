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
    print(f"O texto tem {numero_palavras} palavras") 