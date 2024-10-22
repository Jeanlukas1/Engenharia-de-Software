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