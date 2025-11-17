import tkinter as tk
from tkinter import messagebox
import psycopg2

#Conexão

conn = psycopg2.connect(
    dbname = "testando",
    user = "postgres"
    password = "1907050603Jl@"
    host = "localhost"
)

cur = conn.cursor()

#Cadastrar

def cadastrar():
    try:
        nome_medico = entry_medico.get()
        especialidade = entry_esp.get()
        nome_paciente = entry_paciente.get()
        nascimento = entry_nascimento.get()
        data_consulta = entry_data.get()
        valor = float(entry_valor.get())
        
        cur.execute("INSERT INTO medico (nome, especialidade) VALUES (%s, %s) RETURNING id_medico",
        (nome_medico, especialidade))
        id_medico = cur.fetchone()[0]
        
        cur.execute("INSERT INTO paciente (nome, data_nascimento) VALUES (%s, %s) RETURNING id_paciente",
        (nome_paciente, nascimento))
        id_paciente = cur.fetchone()[0]
        
        cur.execute("INSERT INTO consulta (id_medico, id_paciente, data_consulta, valor) VALUES (%s, %s, %s, %s)"
        (id_medico, id_paciente, data_consulta, valor))
        conn.commit()
        
        messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

    except Exception as e:
        conn.rollback()

        messagebox.showerror("Erro", str(e))
        
def ver_consulta():
    
        