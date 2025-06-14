# Preço com Desconto

# Descrição: Peça o preço original de um produto e a porcentagem de desconto. Calcule e mostre o preço final após o desconto.

# Exemplo de Entrada/Saída:

# Digite o preço original do produto: 100
# Digite a porcentagem de desconto: 15
# O preço com desconto é: 85.0


def Preco_com_Desconto(Po, Por):
    Pf = (Por / 100) * Po
    Vf = Po - Pf

    print(f"""
    ====================================================
    Preço do Produto: {Po:.2f}R$
    Desconto aplicado: {Por}%
    Valor do Desconto: {Pf:.2f}R$
    ----------------------------------------------------
    Preço do produto com desconto: {Vf:.2f}R$
    ====================================================
    """)
    
try:
    Po = float(input("Digite o preço do produto: "))
    Por = int(input("Digite a porcentagem de desconto a ser aplicada em cima do produto: "))
    Preco_com_Desconto(Po, Por)

except ValueError as e:
    print(f"Digite um numero válido: {e}")
    