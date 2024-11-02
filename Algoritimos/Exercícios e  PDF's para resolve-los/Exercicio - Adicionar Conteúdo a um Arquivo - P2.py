#  Adicionar Conteúdo a um Arquivo
#  - Escreva um programa que peça ao usuário para digitar uma frase.
#  - Adicione essa frase ao final de um arquivo existente chamado `anotacoes.txt`

entrada = input("Digite o texto a ser adicionado no projeto")

with open('anotacoes.txt', 'w') as arquivo:
    arquivo.write("Ola mundo, eu sou uma maquina \n")
    
with open('anotacoes.txt', 'a') as arquivo:
    arquivo.writelines(entrada)

with open('anotacoes.txt', 'r') as arquivo:
    ler = arquivo.read()
    print(f"conteudo do arquivo: {ler}")