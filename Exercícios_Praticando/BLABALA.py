lista_de_usuarios = []

def cadastro(email, senha):
    dic_login = {
        "email" : email,
        "senha" : senha
    }
    
    lista_de_usuarios.append(dic_login)
    print("Cadastrado")

def usuarios(lista_de_usuarios):
    if not lista_de_usuarios:
        print("Nenhum usuario Cadastrado!")
    else:
        for user in lista_de_usuarios:
            print("Email:" ,user['email'], "Senha:" ,user['senha'],)
            
    
usuarios(lista_de_usuarios)