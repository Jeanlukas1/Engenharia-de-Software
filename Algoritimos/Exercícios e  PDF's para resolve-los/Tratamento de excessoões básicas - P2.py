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

