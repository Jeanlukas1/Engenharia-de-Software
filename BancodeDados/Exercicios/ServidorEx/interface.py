import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import os

DB_NAME = "exerciciodeconexaodebanco"
DB_USER = "postgres"
DB_PASSWORD = "1907050603Jl@"
DB_HOST = "localhost"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

def insert_aluno():
    conn = None
    nome = entry_nome_aluno.get()
    idade = entry_idade_aluno.get()
    curso = entry_curso_aluno.get()
    
    if nome and idade.isdigit() and curso:
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, int(idade), curso))
            conn.commit()
            messagebox.showinfo("Sucesso", "Dados do aluno inseridos com sucesso!")
        except psycopg2.Error as e:
            messagebox.showerror("Erro no banco", f"{e.pgcode} - {e.pgerror}")
        finally:
            if conn:
                cur.close()
                conn.close()
    else:
        messagebox.showwarning("Erro de entrada", "Preencha todos os campos corretamente.")

def insert_professor():
    conn = None
    nome = entry_nome_prof.get()
    disciplina = entry_disciplina_prof.get()
    
    if nome and disciplina:
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO professores (nome, disciplina) VALUES (%s, %s)", (nome, disciplina))
            conn.commit()
            messagebox.showinfo("Sucesso", "Dados do professor inseridos com sucesso!")
        except psycopg2.Error as e:
            messagebox.showerror("Erro no banco", f"{e.pgcode} - {e.pgerror}")
        finally:
            if conn:
                cur.close()
                conn.close()
    else:
        messagebox.showwarning("Erro de entrada", "Preencha todos os campos corretamente.")

def fetch_data():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, nome, idade, curso FROM alunos")
        alunos = cur.fetchall()
        
        cur.execute("SELECT id, nome, disciplina FROM professores")
        professores = cur.fetchall()

        for row in tree_alunos.get_children():
            tree_alunos.delete(row)
        for row in alunos:
            tree_alunos.insert("", "end", values=row)

        for row in tree_prof.get_children():
            tree_prof.delete(row)
        for row in professores:
            tree_prof.insert("", "end", values=row)

        messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
    except psycopg2.Error as e:
        messagebox.showerror("Erro no banco", f"{e.pgcode} - {e.pgerror}")
    finally:
        if conn:
            cur.close()
            conn.close()

root = tk.Tk()
root.title("Cadastro de Alunos e Professores")


tk.Label(root, text="Nome do Aluno").grid(row=0, column=0)
entry_nome_aluno = tk.Entry(root)
entry_nome_aluno.grid(row=0, column=1)

tk.Label(root, text="Idade do Aluno").grid(row=1, column=0)
entry_idade_aluno = tk.Entry(root)
entry_idade_aluno.grid(row=1, column=1)

tk.Label(root, text="Curso do Aluno").grid(row=2, column=0)
entry_curso_aluno = tk.Entry(root)
entry_curso_aluno.grid(row=2, column=1)

tk.Button(root, text="Cadastrar Aluno", command=insert_aluno).grid(row=3, columnspan=2)


tk.Label(root, text="Nome do Professor").grid(row=4, column=0)
entry_nome_prof = tk.Entry(root)
entry_nome_prof.grid(row=4, column=1)

tk.Label(root, text="Disciplina").grid(row=5, column=0)
entry_disciplina_prof = tk.Entry(root)
entry_disciplina_prof.grid(row=5, column=1)

tk.Button(root, text="Cadastrar Professor", command=insert_professor).grid(row=6, columnspan=2)

tk.Label(root, text="Alunos").grid(row=7, column=0, columnspan=2)
columns_aluno = ("ID", "Nome", "Idade", "Curso")
tree_alunos = ttk.Treeview(root, columns=columns_aluno, show="headings")
for col in columns_aluno:
    tree_alunos.heading(col, text=col)
tree_alunos.grid(row=8, column=0, columnspan=2, sticky='nsew')

tk.Label(root, text="Professores").grid(row=9, column=0, columnspan=2)
columns_prof = ("ID", "Nome", "Disciplina")
tree_prof = ttk.Treeview(root, columns=columns_prof, show="headings")
for col in columns_prof:
    tree_prof.heading(col, text=col)
tree_prof.grid(row=10, column=0, columnspan=2, sticky='nsew')

tk.Button(root, text="Mostrar Dados", command=fetch_data).grid(row=11, columnspan=2)

root.mainloop()