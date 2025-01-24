lista_de_usuarios = []

def cadastro(email, senha):
    dic_login = {
        "email" : email,
        "senha" : senha
    }
    
   lista_de_usuarios.append(dic_login)
   
email = input("Email: ")
senha = float(input("Senha: "))