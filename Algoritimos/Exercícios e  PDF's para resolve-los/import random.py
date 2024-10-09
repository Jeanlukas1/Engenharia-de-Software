import random
import string

def gerar_senha(tamanho):
    if tamanho == 0:
        return ""
    else:
        caracteres = string.ascii_letters + string.digits
        caractere = random.choice(caracteres)
        return caractere + gerar_senha(tamanho - 1)

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        elif char.isdigit():
            resultado += chr((ord(char) - ord('0') + deslocamento) % 10 + ord('0'))
        else:
            resultado += char
    return resultado

def main(tamanho_senha):
    senha = gerar_senha(tamanho_senha)
    print("Senha original:", senha)
    senha_criptografada = cifra_de_cesar(senha, 3)
    print("Senha criptografada:", senha_criptografada)

main(8)  
