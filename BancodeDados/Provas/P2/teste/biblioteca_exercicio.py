"""
EXERCÍCIO - Sistema de Biblioteca com Tkinter
Complete as funções que estão marcadas com # TODO
Siga o padrão do arquivo sql_tkinter.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from psycopg2 import Error as PsycopgError


DB_NAME = "revisaop2"
DB_USER = "postgres"
DB_PASSWORD = "univassouras"
DB_HOST = "localhost"



def get_connection():
    """Abre conexão com o PostgreSQL"""
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )


def inserir_emprestimo():
    conn = None
    id_livro = entry_livro_id.get()
    id_usuario = entry_usuario_id.get()

    if id_livro and id_usuario:
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO emprestimos (livro_id, usuario_id) VALUES (%s, %s)", (id_livro, id_usuario))
            conn.commit()
            messagebox.showinfo("Sucesso", "Empréstimo cadastrado!")
            entry_livro_id.delete(0, tk.END)
            entry_usuario_id.delete(0, tk.END)
            buscar_emprestimos()
        except PsycopgError as e:
            messagebox.showerror("Erro", f"Erro: {e}")
        finally:
            if conn:
                cur.close()
                conn.close()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")


def buscar_emprestimos():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                e.id,
                l.titulo,
                u.nome,
                e.data_emprestimo,
                e.status
            FROM emprestimos e
            INNER JOIN livros l ON e.livro_id = l.id
            INNER JOIN usuarios u ON e.usuario_id = u.id
            ORDER BY e.id DESC
        """)
        resultados = cur.fetchall()

        for item in tree_emprestimos.get_children():
            tree_emprestimos.delete(item)

        for row in resultados:
            tree_emprestimos.insert("", "end", values=row)
    except PsycopgError as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


def atualizar_status():
    conn = None
    selecionado = tree_emprestimos.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um empréstimo!")
        return

    item = tree_emprestimos.item(selecionado[0])
    emprestimo_id = item['values'][0]

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE emprestimos SET status = 'devolvido' WHERE id = %s", (emprestimo_id,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Status atualizado!")
        buscar_emprestimos()
    except PsycopgError as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


def excluir_emprestimo():
    conn = None
    selecionado = tree_emprestimos.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um empréstimo!")
        return

    if not messagebox.askyesno("Confirmar", "Deseja realmente excluir?"):
        return

    item = tree_emprestimos.item(selecionado[0])
    emprestimo_id = item['values'][0]

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM emprestimos WHERE id = %s", (emprestimo_id,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Empréstimo excluído!")
        buscar_emprestimos()
    except PsycopgError as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


def buscar_logs():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                id,
                operacao_descritiva,
                emprestimo_id,
                COALESCE(usuario_responsavel, 'Sistema') as usuario,
                TO_CHAR(data_hora, 'DD/MM/YYYY HH24:MI:SS') as data_formatada
            FROM view_logs_completa
            ORDER BY data_hora DESC
            LIMIT 100
        """)
        resultados = cur.fetchall()

        for item in tree_logs.get_children():
            tree_logs.delete(item)

        for row in resultados:
            tree_logs.insert("", "end", values=row)
    except PsycopgError as e:
        messagebox.showerror("Erro", f"Erro ao buscar logs: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


root = tk.Tk()
root.title("Sistema de Biblioteca - Exercício")
root.geometry("1000x600")


frame_inserir = tk.LabelFrame(root, text="Novo Empréstimo", padx=10, pady=10)
frame_inserir.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame_inserir, text="ID Livro:").grid(row=0, column=0, padx=5, pady=5)
entry_livro_id = tk.Entry(frame_inserir, width=20)
entry_livro_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inserir, text="ID Usuário:").grid(
    row=0, column=2, padx=5, pady=5)
entry_usuario_id = tk.Entry(frame_inserir, width=20)
entry_usuario_id.grid(row=0, column=3, padx=5, pady=5)

tk.Button(frame_inserir, text="Inserir Empréstimo", command=inserir_emprestimo,
          bg="#27ae60", fg="white", padx=10).grid(row=0, column=4, padx=5)


frame_acoes = tk.Frame(root)
frame_acoes.pack(fill=tk.X, padx=10, pady=5)

tk.Button(frame_acoes, text="Atualizar Status", command=atualizar_status,
          bg="#3498db", fg="white", padx=10).pack(side=tk.LEFT, padx=5)

tk.Button(frame_acoes, text="Excluir", command=excluir_emprestimo,
          bg="#e74c3c", fg="white", padx=10).pack(side=tk.LEFT, padx=5)

tk.Button(frame_acoes, text="🔄 Atualizar Lista", command=buscar_emprestimos,
          bg="#95a5a6", fg="white", padx=10).pack(side=tk.LEFT, padx=5)


notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)


frame_emprestimos = tk.Frame(notebook)
notebook.add(frame_emprestimos, text="Empréstimos")


scrollbar_emp = tk.Scrollbar(frame_emprestimos)
scrollbar_emp.pack(side=tk.RIGHT, fill=tk.Y)

tree_emprestimos = ttk.Treeview(
    frame_emprestimos,
    columns=("ID", "Livro", "Usuário", "Data Empréstimo", "Status"),
    show="headings",
    yscrollcommand=scrollbar_emp.set
)

tree_emprestimos.heading("ID", text="ID")
tree_emprestimos.heading("Livro", text="Livro")
tree_emprestimos.heading("Usuário", text="Usuário")
tree_emprestimos.heading("Data Empréstimo", text="Data Empréstimo")
tree_emprestimos.heading("Status", text="Status")

tree_emprestimos.column("ID", width=50)
tree_emprestimos.column("Livro", width=200)
tree_emprestimos.column("Usuário", width=150)
tree_emprestimos.column("Data Empréstimo", width=120)
tree_emprestimos.column("Status", width=100)

tree_emprestimos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_emp.config(command=tree_emprestimos.yview)

# Aba Logs
frame_logs = tk.Frame(notebook)
notebook.add(frame_logs, text="Log de Operações")

tk.Button(frame_logs, text="🔄 Atualizar Logs", command=buscar_logs,
          bg="#9b59b6", fg="white", padx=10).pack(pady=5)

scrollbar_log = tk.Scrollbar(frame_logs)
scrollbar_log.pack(side=tk.RIGHT, fill=tk.Y)

tree_logs = ttk.Treeview(
    frame_logs,
    columns=("ID", "Operação", "Empréstimo ID", "Usuário", "Data/Hora"),
    show="headings",
    yscrollcommand=scrollbar_log.set
)

tree_logs.heading("ID", text="ID")
tree_logs.heading("Operação", text="Operação")
tree_logs.heading("Empréstimo ID", text="Empréstimo ID")
tree_logs.heading("Usuário", text="Usuário Responsável")
tree_logs.heading("Data/Hora", text="Data/Hora")

tree_logs.column("ID", width=50)
tree_logs.column("Operação", width=120)
tree_logs.column("Empréstimo ID", width=100)
tree_logs.column("Usuário", width=150)
tree_logs.column("Data/Hora", width=180)

tree_logs.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_log.config(command=tree_logs.yview)


buscar_emprestimos()
buscar_logs()

root.mainloop()
