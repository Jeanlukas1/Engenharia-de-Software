import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from psycopg2.extras import RealDictCursor

# -------------------- CONFIGURAÇÕES DO BANCO --------------------
DB_NAME = "biblioteca_db"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = None
DB_PASSWORD = None

# -------------------- CONEXÃO COM O BANCO --------------------
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# -------------------- CLASSE PRINCIPAL --------------------
class BibliotecaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📚 Sistema de Biblioteca")
        self.geometry("900x500")
        self.resizable(True, True)

        # Conectar ao banco
        try:
            self.conn = get_connection()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar ao banco:\n{e}")
            self.destroy()
            return

        # Interface de abas
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill="both", expand=True)

        self.tab_view = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_view, text="📖 Empréstimos")

        if DB_USER == "bibl_admin":
            self.tab_crud = ttk.Frame(self.tabs)
            self.tab_logs = ttk.Frame(self.tabs)
            self.tabs.add(self.tab_crud, text="⚙️ Gerenciar")
            self.tabs.add(self.tab_logs, text="📝 Logs")

        self.create_view_tab()
        if DB_USER == "bibl_admin":
            self.create_crud_tab()
            self.create_logs_tab()

    # -------------------- ABA DE VISUALIZAÇÃO --------------------
    def create_view_tab(self):
        ttk.Label(self.tab_view, text="Empréstimos Gerais", font=("Arial", 14, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(self.tab_view, columns=("id", "livro", "usuario", "data_emp", "data_dev", "status"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("livro", text="Livro")
        self.tree.heading("usuario", text="Usuário")
        self.tree.heading("data_emp", text="Data Empréstimo")
        self.tree.heading("data_dev", text="Data Devolução")
        self.tree.heading("status", text="Status")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(self.tab_view, text="🔄 Atualizar", command=self.load_view).pack(pady=5)
        self.load_view()

    def load_view(self):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            cur.execute('SELECT * FROM vw_emprestimos_geral ORDER BY id_emprestimo DESC')
            rows = cur.fetchall()
            cur.close()

            for i in self.tree.get_children():
                self.tree.delete(i)

            for r in rows:
                self.tree.insert("", "end", values=(
                    r.get('id_emprestimo'),
                    r.get('titulo_livro'),
                    r.get('nome_usuario'),
                    r.get('data_emprestimo'),
                    r.get('data_devolucao') or '',
                    r.get('status_descricao')
                ))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar view:\n{e}")

    # -------------------- ABA DE CRUD (ADMIN) --------------------
    def create_crud_tab(self):
        frame = ttk.Frame(self.tab_crud)
        frame.pack(pady=10)

        ttk.Label(frame, text="ID Usuário:").grid(row=0, column=0, padx=5, pady=5)
        self.id_user = ttk.Entry(frame)
        self.id_user.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="ID Livro:").grid(row=1, column=0, padx=5, pady=5)
        self.id_book = ttk.Entry(frame)
        self.id_book.grid(row=1, column=1, padx=5)

        ttk.Button(frame, text="➕ Inserir Empréstimo", command=self.insert_loan).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="📤 Devolver Empréstimo", command=self.return_loan).grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(frame, text="❌ Excluir Empréstimo", command=self.delete_loan).grid(row=4, column=0, columnspan=2, pady=5)

    def insert_loan(self):
        try:
            id_u = self.id_user.get().strip()
            id_l = self.id_book.get().strip()
            if not id_u or not id_l:
                messagebox.showwarning("Aviso", "Preencha ID do usuário e ID do livro.")
                return
            cur = self.conn.cursor()
            cur.execute("INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (%s, %s, CURRENT_DATE);", (id_u, id_l))
            self.conn.commit()
            cur.close()
            self.load_view()
            messagebox.showinfo("Sucesso", "Empréstimo registrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao inserir empréstimo:\n{e}")

    def return_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um empréstimo para devolver.")
            return
        try:
            item = self.tree.item(selected[0])
            id_emprestimo = item["values"][0]
            cur = self.conn.cursor()
            cur.execute("UPDATE emprestimos SET data_devolucao = CURRENT_DATE, status='devolvido' WHERE id = %s;", (id_emprestimo,))
            self.conn.commit()
            cur.close()
            self.load_view()
            messagebox.showinfo("Sucesso", "Livro devolvido!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao devolver:\n{e}")

    def delete_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um empréstimo para excluir.")
            return
        try:
            item = self.tree.item(selected[0])
            id_emprestimo = item["values"][0]
            cur = self.conn.cursor()
            cur.execute("DELETE FROM emprestimos WHERE id = %s;", (id_emprestimo,))
            self.conn.commit()
            cur.close()
            self.load_view()
            messagebox.showinfo("Sucesso", "Empréstimo excluído!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao excluir:\n{e}")

    # -------------------- ABA DE LOGS (ADMIN) --------------------
    def create_logs_tab(self):
        ttk.Label(self.tab_logs, text="Logs de Empréstimos", font=("Arial", 14, "bold")).pack(pady=10)
        self.tree_logs = ttk.Treeview(self.tab_logs, columns=("id", "acao", "id_emprestimo", "usuario", "data"), show="headings")
        self.tree_logs.heading("id", text="ID Log")
        self.tree_logs.heading("acao", text="Ação")
        self.tree_logs.heading("id_emprestimo", text="ID Empréstimo")
        self.tree_logs.heading("usuario", text="Usuário")
        self.tree_logs.heading("data", text="Data")
        self.tree_logs.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(self.tab_logs, text="🔄 Atualizar Logs", command=self.load_logs).pack(pady=5)
        self.load_logs()

    def load_logs(self):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            cur.execute('SELECT id_log, operacao, id_emprestimo, usuario_db, quando FROM emprestimos_log ORDER BY id_log DESC LIMIT 500')
            rows = cur.fetchall()
            cur.close()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao carregar logs: {e}')
            return

        for r in self.tree_logs.get_children():
            self.tree_logs.delete(r)
        for row in rows:
            self.tree_logs.insert('', 'end', values=(
                row.get('id_log'),
                row.get('operacao'),
                row.get('id_emprestimo'),
                row.get('usuario_db'),
                str(row.get('quando'))
            ))

# -------------------- TELA DE LOGIN --------------------
def login_screen():
    login = tk.Tk()
    login.title("Login - Biblioteca")
    login.geometry("300x200")
    login.resizable(False, False)

    tk.Label(login, text="Usuário:").pack(pady=(20,5))
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Senha:").pack(pady=(10,5))
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack()

    def autenticar():
        global DB_USER, DB_PASSWORD
        DB_USER = user_entry.get().strip()
        DB_PASSWORD = pass_entry.get().strip()
        if not DB_USER or not DB_PASSWORD:
            messagebox.showwarning("Aviso", "Preencha usuário e senha.")
            return
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            conn.close()
            messagebox.showinfo("Sucesso", f"Login bem-sucedido como {DB_USER}")
            login.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na conexão:\n{e}")

    tk.Button(login, text="Entrar", width=15, command=autenticar).pack(pady=15)
    login.bind("<Return>", lambda e: autenticar())

    login.lift()
    login.attributes('-topmost', True)
    login.after_idle(login.attributes, '-topmost', False)
    login.mainloop()

# -------------------- EXECUÇÃO PRINCIPAL --------------------
if __name__ == '__main__':
    print("🔐 Abrindo tela de login...")
    login_screen()

    if not DB_USER or not DB_PASSWORD:
        print("❌ Login cancelado. Encerrando aplicação.")
    else:
        print(f"✅ Usuário autenticado: {DB_USER}")
        app = BibliotecaApp()

        app.lift()
        app.attributes('-topmost', True)
        app.after_idle(app.attributes, '-topmost', False)

        print("🚀 Executando interface Tkinter...")
        app.mainloop()
        print("🛑 Aplicação encerrada.")
