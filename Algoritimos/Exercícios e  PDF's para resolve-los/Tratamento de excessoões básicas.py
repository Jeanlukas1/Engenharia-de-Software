# 1. Tratamento de exceções básicas: Escreva um programa que peça ao usuário
# dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir
# um valor inválido ou tentar dividir por zero, o programa deve exibir uma
# mensagem de erro apropriada.

def div(num1, num2):
    divisao = num1 / num2
    return divisao

try: 
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    resultado = div(num1, num2)
    print(resultado)

except ZeroDivisionError:
    print("Não é possivel divisão por zero")

except ValueError:
    print("Digite um numero valido!")


#2. Capturando exceções múltiplas: Crie um programa que peça ao usuário o
# nome de uma cor e mostre seu valor em RGB de acordo com um dicionário
# pré-definido. O programa deve tratar exceções caso o nome da cor não exista
# no dicionário.

cores = {
    "vermelho": (255, 0, 0), 
    "verde": (0, 255, 0), 
    "azul":(0, 0, 255)
    }

entrada = input("Digite a cor desejada: ")

if entrada not in cores:
    raise KeyError("Cor nao encontrada na lista")
elif entrada == "vermelho":
    print(f"Essa é a cor de {entrada} em RGB: {cores["vermelho"]}")
elif entrada == "verde":
    print(f"Essa é a cor de {entrada} em RGB: {cores["verde"]}")
elif entrada == "azul":
    print(f"Essa é a cor de {entrada} em RGB: {cores["azul"]}")


#3. Bloco else e finally: Escreva um programa que solicite um número ao
# usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
# número é válido. Utilize o bloco else para imprimir que o programa foi
# executado com sucesso, e o bloco finally para imprimir "Programa
# encerrado"

# def numero(num):
#     return num

# try:
#     num = int(input("Digite um numero: "))
#     if num >= 10:
#         print("Número válido")
#     else:
#         print("Programa executado com sucesso!")
#     resultado = numero(num)
#     print(resultado)

# finally:
#     print("Programa encerrado!")