import tkinter as tk
from tkinter import messagebox
import psycopg2

# Conecção:
conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "univassouras",
    host = "localhost"
)
cur = conn.cursor()

# Cadastrar:
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

        cur.execute("INSERT INTO consulta (id_medico, id_paciente, data_consulta, valor) VALUES (%s, %s, %s, %s)",
        (id_medico, id_paciente, data_consulta, valor))
        conn.commit()

        messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

    except Exception as e:
        conn.rollback()

        messagebox.showerror("Erro", str(e))

# Ver consultas:
def ver_consultas():
    try:
        cur.execute("SELECT * FROM consulta")
        dados = cur.fetchall()
        texto = "\n".join([f"{row[0]} - {row[1]} - {row[2]} - R${row[3]:.2f}" for row in dados])
        
        messagebox.showinfo("main_view", texto)

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Tkinter view:
root = tk.Tk()
root.title("Cadastro de Consultas Médicas")

entry_medico = tk.Entry(root); entry_medico.pack(); entry_medico.insert(0, "Dr Who")
entry_esp = tk.Entry(root); entry_esp.pack(); entry_esp.insert(0, "Clinico Geral")

entry_paciente = tk.Entry(root); entry_paciente.pack(); entry_paciente.insert(0, "Marcos")
entry_nascimento = tk.Entry(root); entry_nascimento.pack(); entry_nascimento.insert(0, "1990-05-10")

entry_data = tk.Entry(root); entry_data.pack(); entry_data.insert(0, "2025-03-15 15:00")
entry_valor = tk.Entry(root); entry_valor.pack(); entry_valor.insert(0, 200)

btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
btn_cadastrar.pack()

btn_ver = tk.Button(root, text="Ver Consultas", command=ver_consultas)
btn_ver.pack()

root.mainloop()
