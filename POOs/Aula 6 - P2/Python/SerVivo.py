class SerVivo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def respirar(self):
        print(f"{self.nome} está respirando.")

    def mover(self):
        print(f"{self.nome} está se movendo.")

# Classe Humano que herda de SerVivo
class Humano(SerVivo):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como {self.profissao}.")

# Testando
humano1 = Humano("Alice", 30, "Engenheira")
humano1.respirar()
humano1.mover()
humano1.trabalhar()
