
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "0":
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if op == "1":
        print("Resultado:", soma(a, b))
    elif op == "2":
        print("Resultado:", sub(a, b))
    elif op == "3":
        print("Resultado:", mult(a, b))
    elif op == "4":
        print("Resultado:", div(a, b))
    else:
        print("Opção inválida!")
