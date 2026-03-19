# Exercício 1: Sistema de Cadastro Simples
# Crie um sistema que permita cadastrar nomes e listar todos

usuarios = []

def cadastrar():
    nome = input("Digite o nome: ")
    usuarios.append(nome)
    print("Usuário cadastrado!")

def listar():
    print("\nLista de usuários:")
    for u in usuarios:
        print("-", u)

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "0":
        break
    else:
        print("Opção inválida!")
