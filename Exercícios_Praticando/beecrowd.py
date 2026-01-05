# Leitura dos dados
import math

x1, y1 = map(float, input("Digite o valor de x1 e y1 (ex: 10 20): ").split())
x2, y2 = map(float, input("Digite o valor de x2 e y2 (ex: 10 20): ").split())

distancia = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)

print(f"Distancia entre os dois pontos é: {distancia:.4f}")