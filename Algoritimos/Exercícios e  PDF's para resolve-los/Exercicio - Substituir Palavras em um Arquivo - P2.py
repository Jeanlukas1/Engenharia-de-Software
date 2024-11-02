
# Substituir Palavras em um Arquivo
#  - Crie um programa que leia o conteúdo de um arquivo `texto.txt`.
#  - Substitua todas as ocorrências de uma palavra (por exemplo, "Python") por outra (por
#  exemplo, "programação") e salve o conteúdo alterado em um novo arquivo chamado
# `texto_modificado.txt`.

with open('texto2.txt', 'w') as arquivo1:
    arquivo1.write("Ola mundo, eu sou uma maquina \n")
    arquivo1.write("Ola mundo, eu sou uma maquina \n")
    arquivo1.write("Ola mundo, eu sou uma maquina \n")

with open('texto3.txt', 'w') as arquivo:
    texto = arquivo1
    novo_texto = ("mundo", "python")
    arquivo.write("Modificado!")
