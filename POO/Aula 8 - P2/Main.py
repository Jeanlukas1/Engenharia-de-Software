import tkinter as tk
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        raise NotImplementedError("Subclasse deve implementar o método apresentar().")

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        return f"Sou o aluno {self.nome} e curso {self.curso}."

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Sou o professor {self.nome} e leciono {self.disciplina}."

def apresentar_pessoa(pessoa: Pessoa):
    return pessoa.apresentar()


class SistemaApresentacoes:
    def __init__(self, pessoas):
        self.pessoas = pessoas
        
        self.janela = tk.Tk()
        self.janela.title("Sistema de Apresentações")
        self.janela.geometry("300x200")

        self.botao = tk.Button(self.janela, text="Mostrar Apresentações", command=self.apresentar_pessoas)
        self.botao.pack(pady=40)

        botao_fechar = tk.Button(self.janela, text="Fechar todas", command=self.fechar)
        botao_fechar.pack()

        
    def apresentar_pessoas(self):

        mensagens = [apresentar_pessoa(p) for p in self.pessoas]

        messagebox.showinfo("Apresentações", "\n".join(mensagens))


    def iniciar(self):
        self.janela.mainloop()
    
    def fechar():
        for janela in tk.winfo_children():
            if janela.winfo_children(): # Verifica se a janela tem filhos (ex: janelas de diálogo)
                janela.destroy()

aluno = Aluno("Zé da Manga", "Engenharia de Software")
professor = Professor("Zé da Couve", "POO")
pessoas = [aluno, professor]

sistema = SistemaApresentacoes(pessoas)
sistema.iniciar()
