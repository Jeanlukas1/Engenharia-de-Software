#1. Implemente uma função recursiva que calcule a potência de um número (base^expoente)

def calcular_potencia(base, expoente):
    if expoente == 0:
        return 1
    elif expoente == 1:
        return base
    else:
        return base * calcular_potencia(base, expoente - 1)

resultado = calcular_potencia(2, 3)
print(resultado)

# 2. Crie uma função recursiva para calcular o n-ésimo termo da sequência de 
# Fibonacci.Lembre-se de que a sequência começa com 0 e 1

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
resultado = fibonacci(5)

print(resultado)

# 3. Escreva uma função recursiva que conte quantos dígitos um número tem.

def digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + digitos(num // 10)

resultado = digitos(65)
print(resultado)

#4. Escreva uma função recursiva que verifique se uma string é um palíndromo. 
   
def verificar_palindromo(str):
    if len(str) <= 1:
        return "é palindromo"
        
    if str[0] != str[-1]:
        return "não é palindromo"
    
    return verificar_palindromo(str[1:-1])
    
resultado = verificar_palindromo("pop")
print(resultado)