# Leitura dos dados
for i in range(2):
    codigo1 = int(input(f"Digite o codigo da peça {i+1}: "))
    num1 = int(input(f"Digite a quantidade de peças {i+1}: "))
    valor1 = float(input(f"Digite o valor da peça {i+1}: "))

total = (num1 * valor1) + (num1 * valor1)

print(f"Total: R$ {total:.2f}")