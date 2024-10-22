# 3. Bloco else e finally: Escreva um programa que solicite um número ao
# usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
# número é válido. Utilize o bloco else para imprimir que o programa foi
# executado com sucesso, e o bloco finally para imprimir "Programa
# encerrado"

def numero(num):
    return num

try:
    num = int(input("Digite um numero: "))
    if num >= 10:
        print("Número válido")
    else:
        print("Programa executado com sucesso!")
    resultado = numero(num)
    print(resultado)

finally:
    print("Programa encerrado!")