# Tempo em Minutos

# Descrição: Leia uma quantidade de dias e converta esse valor para o total de minutos.

# Exemplo de Entrada/Saída:

# Digite a quantidade de dias: 2
# O total em minutos é: 2880

try:
    def saber_min(dias):
        min = 1440
        resultado = min * dias
        print(f"O total em min é: {resultado}")
        
except ValueError:
    print(f"Digite um número válido (OBS: Somente numeros inteiros) {ValueError}")


dias = int(input("Digite a quantidade de dias que deseja retornar em minutos: "))

saber_min(dias)
