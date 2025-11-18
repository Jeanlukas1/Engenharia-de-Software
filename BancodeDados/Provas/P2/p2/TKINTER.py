import tkinter as tk 
from tkinter import messagebox 
import psycopg2
 
# ----------------------------- 
# Função principal para executar SQL livre 
# ----------------------------- 
def executar_sql(): 
    try: 
        usuario = entry_user.get() 
        senha = entry_pass.get() 
        banco = entry_db.get() 
        comando = entry_sql.get("1.0", "end") 
 
        conn = psycopg2.connect( 
            dbname=banco, 
            user=usuario, 
            password=senha, 
            host="localhost" 
        ) 
        cur = conn.cursor() 
        cur.execute(comando) 
 
        if comando.strip().lower().startswith("select"): 
            dados = cur.fetchall() 
            texto = "\n".join([str(row) for row in dados]) 
            messagebox.showinfo("Resultado", texto) 
        else: 
            conn.commit() 
            messagebox.showinfo("Sucesso", "Comando executado!") 
 
    except Exception as e: 
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}") 
 
# ----------------------------- 
# CADASTRAR DEPARTAMENTO 
# ----------------------------- 
def cadastrar_departamento(): 
    try: 
        usuario = entry_user.get() 
        senha = entry_pass.get() 
        banco = entry_db.get()
        host = entry_host.get()
 
        nome_dep = entry_dep_nome.get() 
 
        conn = psycopg2.connect( 
            dbname=banco, 
            user=usuario, 
            password=senha, 
            host=host 
        ) 
        cur = conn.cursor() 
 
        cur.execute("INSERT INTO departamentos (nome) VALUES (%s) ",(nome_dep))

        conn.commit() 
        messagebox.showinfo("Cadastro", "Departamento cadastrado!") 
 
    except Exception as e: 
        messagebox.showerror("Erro", f"{e}") 
 
# ----------------------------- 
# CADASTRAR FUNCIONÁRIO 
# ----------------------------- 
def cadastrar_funcionario(): 
    try: 
        usuario = entry_user.get() 
        senha = entry_pass.get() 
        banco = entry_db.get() 
        host = entry_host.get()
 
        nome = entry_fun_nome.get() 
        cargo = entry_fun_cargo.get() 
        salario = entry_fun_salario.get() 
        id_dep = entry_fun_dep.get() 
 
        conn = psycopg2.connect( 
            dbname=banco, 
            user=usuario, 
            password=senha, 
            host=host 
        ) 
        cur = conn.cursor() 
 
        cur.execute(""" 
            INSERT INTO funcionarios (nome, cargo, salario, id_departamento) 
            VALUES (%s, %s, %s, %s) 
        """, (nome, cargo, salario, id_dep)) 
        conn.commit() 
        messagebox.showinfo("Cadastro", "Funcionário cadastrado!") 
 
    except Exception as e: 
        messagebox.showerror("Erro", f"{e}") 
 
# ----------------------------- 
# CADASTRAR PROJETO 
# ----------------------------- 
def cadastrar_projeto(): 
    try: 
        usuario = entry_user.get() 
        senha = entry_pass.get() 
        banco = entry_db.get()
        host = entry_host.get()
 
        nome = entry_proj_nome.get() 
        descricao = entry_proj_desc.get() 
        id_dep = entry_proj_dep.get() 
 
        conn = psycopg2.connect( 
            dbname=banco, 
            user=usuario, 
            password=senha, 
            host=host 
        ) 
        cur = conn.cursor() 
 
        cur.execute(""" 
            INSERT INTO projetos (nome, descricao, id_departamento) 
            VALUES (%s, %s, %s) 
        """, (nome, descricao, id_dep)) 
 
        conn.commit() 
        messagebox.showinfo("Cadastro", "Projeto cadastrado!") 
 
    except Exception as e: 
        messagebox.showerror("Erro", f"{e}") 
 
# ----------------------------- 
# INTERFACE TKINTER 
# ----------------------------- 
janela = tk.Tk() 
janela.title("Gerenciador de Banco – PostgreSQL") 
 
# AUTENTICAÇÃO 
tk.Label(janela, text="Usuário:").grid(row=0, column=0) 
entry_user = tk.Entry(janela) 
entry_user.grid(row=0, column=1) 
 
tk.Label(janela, text="Senha:").grid(row=1, column=0) 
entry_pass = tk.Entry(janela, show="*") 
entry_pass.grid(row=1, column=1) 
 
tk.Label(janela, text="Banco:").grid(row=2, column=0) 
entry_db = tk.Entry(janela) 
entry_db.grid(row=2, column=1)

tk.Label(janela, text="Host: ").grid(row=3, column=0) 
entry_host = tk.Entry(janela) 
entry_host.grid(row=3, column=1)
 
# EXECUTOR SQL 
tk.Label(janela, text="SQL Livre:").grid(row=4, column=0) 
entry_sql = tk.Text(janela, height=4, width=45) 
entry_sql.grid(row=4, column=1) 
 
tk.Button(janela, text="Executar SQL", command=executar_sql).grid(row=4, column=1) 
 
# ----------------------------- 
# SEÇÃO: CADASTRO DE DEPARTAMENTO 
# ----------------------------- 
tk.Label(janela, text="--- Cadastrar Departamento ---").grid(row=5, column=0, columnspan=2) 
 
tk.Label(janela, text="Nome do Departamento:").grid(row=6, column=0) 
entry_dep_nome = tk.Entry(janela) 
entry_dep_nome.grid(row=6, column=1) 
 
tk.Button(janela,  text="Cadastrar  Departamento",  command=cadastrar_departamento).grid(row=7, 
column=1) 
 
# ----------------------------- 
# SEÇÃO: CADASTRO DE FUNCIONÁRIOS 
# ----------------------------- 
tk.Label(janela, text="--- Cadastrar Funcionário ---").grid(row=8, column=0, columnspan=2) 
 
tk.Label(janela, text="Nome:").grid(row=9, column=0) 
entry_fun_nome = tk.Entry(janela) 
entry_fun_nome.grid(row=9, column=1) 
 
tk.Label(janela, text="Cargo:").grid(row=10, column=0) 
entry_fun_cargo = tk.Entry(janela) 
entry_fun_cargo.grid(row=10, column=1) 
 
tk.Label(janela, text="Salário:").grid(row=11, column=0) 
entry_fun_salario = tk.Entry(janela) 
entry_fun_salario.grid(row=11, column=1) 
 
tk.Label(janela, text="ID Departamento:").grid(row=12, column=0) 
entry_fun_dep = tk.Entry(janela) 
entry_fun_dep.grid(row=12, column=1) 
 
tk.Button(janela, text="Cadastrar Funcionário", command=cadastrar_funcionario).grid(row=13, 
column=1) 
 
# ----------------------------- 
# SEÇÃO: CADASTRO DE PROJETOS 
# ----------------------------- 
tk.Label(janela, text="--- Cadastrar Projeto ---").grid(row=14, column=0, columnspan=2) 
 
tk.Label(janela, text="Nome Projeto:").grid(row=15, column=0) 
entry_proj_nome = tk.Entry(janela) 
entry_proj_nome.grid(row=15, column=1) 
 
tk.Label(janela, text="Descrição:").grid(row=16, column=0) 
entry_proj_desc = tk.Entry(janela) 
entry_proj_desc.grid(row=16, column=1) 
 
tk.Label(janela, text="ID Departamento:").grid(row=17, column=0) 
entry_proj_dep = tk.Entry(janela) 
entry_proj_dep.grid(row=17, column=1) 
 
tk.Button(janela, text="Cadastrar Projeto", command=cadastrar_projeto).grid(row=18, column=1) 
 
janela.mainloop()