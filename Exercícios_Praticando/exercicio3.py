# Exercício 3: Sistema de Tarefas (POO)

class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✔" if self.concluida else "✘"
        return f"{self.titulo} [{status}]"


class Gerenciador:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo):
        self.tarefas.append(Tarefa(titulo))

    def listar(self):
        for i, t in enumerate(self.tarefas):
            print(i, "-", t)

    def concluir(self, index):
        if 0 <= index < len(self.tarefas):
            self.tarefas[index].concluir()


g = Gerenciador()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        titulo = input("Título: ")
        g.adicionar(titulo)

    elif op == "2":
        g.listar()

    elif op == "3":
        i = int(input("Número da tarefa: "))
        g.concluir(i)

    elif op == "0":
        break
