class Pessoa:
    def __init__(self, nome, genero, cpf):
        self.nome = nome
        self.genero = genero
        self.cpf = cpf

pessoa1 = Pessoa("Joao", "M", "123456")
print(pessoa1.nome)