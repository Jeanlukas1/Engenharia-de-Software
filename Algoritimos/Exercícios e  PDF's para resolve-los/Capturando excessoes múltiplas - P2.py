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

if entrada in cores:
    print(cores[entrada])
    
else:
    raise KeyError("Cor nao encontrada na lista")

