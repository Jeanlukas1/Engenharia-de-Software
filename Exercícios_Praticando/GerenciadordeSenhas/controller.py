from model import Usuario, usr1
from view import nomeSenha

def entrar1(nome, senha):
    return nomeSenha(nome, senha)


print(entrar1(usr1.nome, usr1.senha))
