# 4 - Exceções personalizadas: Escreva uma função que verifica se uma senha 
# possui no mínimo 8 caracteres e pelo menos um número. Se a senha não 
# atender aos requisitos, levante uma exceção com uma mensagem 
# personalizada. Trate a exceção e mostre a mensagem ao usuário. 

class SenhaInvalida(Exception):
    pass

def verificar_senha(senha):
    if len(senha) < 8:
        raise SenhaInvalida("A senha deve ter pelo menos 8 caracteres.")
    
    if not any(char.isdigit() for char in senha):
        raise SenhaInvalida("A senha deve conter pelo menos um número.")

def solicitar_senha():
    senha = input("Digite uma senha: ")
    try:
        verificar_senha(senha)
        print("Senha válida!")
    except SenhaInvalida as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    solicitar_senha()
