# Maior de Três Números

# Descrição: Peça três números ao usuário e exiba o maior deles.

# Exemplo de Entrada/Saída:

# Digite o primeiro número: 12
# Digite o segundo número: 7
# Digite o terceiro número: 15
# O maior número é: 15

p = input("Digite os numeros: ").split()

maior = max(p)

print(p, maior)
