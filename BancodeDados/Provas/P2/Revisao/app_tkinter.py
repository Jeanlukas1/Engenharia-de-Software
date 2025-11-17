import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from psycopg2.extras import RealDictCursor

# -------------------- CONFIG BANCO --------------------
DB_NAME = "biblioteca_db"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = None
DB_PASSWORD = None


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
        self.geometry("1000x600")
        self.resizable(True, True)

        try:
            self.conn = get_connection()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar ao banco:\n{e}")
            self.destroy()
            return

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

    # -------------------- VIEW --------------------
    def create_view_tab(self):
        ttk.Label(self.tab_view, text="Empréstimos Gerais", font=("Arial", 14, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(
            self.tab_view,
            columns=("id", "livro", "usuario", "data_emp", "data_dev"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("livro", text="Livro")
        self.tree.heading("usuario", text="Usuário")
        self.tree.heading("data_emp", text="Data Empréstimo")
        self.tree.heading("data_dev", text="Data Devolução")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(self.tab_view, text="🔄 Atualizar", command=self.load_view).pack(pady=5)
        self.load_view()

    def load_view(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM vw_emprestimos_geral ORDER BY id;")
            rows = cur.fetchall()
            cur.close()

            for i in self.tree.get_children():
                self.tree.delete(i)

            for r in rows:
                self.tree.insert("", "end", values=r)

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar view:\n{e}")

    # -------------------- CRUD ADMIN --------------------
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
            cur.execute("""
                INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo)
                VALUES (%s, %s, CURRENT_DATE)
                RETURNING id;
            """, (id_u, id_l))

            emp_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO emprestimos_log (operacao, id_emprestimo, usuario_db)
                VALUES ('INSERIR', %s, %s)
            """, (emp_id, DB_USER))

            self.conn.commit()
            cur.close()

            self.load_view()
            messagebox.showinfo("Sucesso", "Empréstimo registrado!")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao inserir empréstimo:\n{e}")

    def return_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um empréstimo.")
            return

        try:
            item = self.tree.item(selected[0])
            id_emprestimo = item["values"][0]

            cur = self.conn.cursor()
            cur.execute("""
                UPDATE emprestimos 
                SET data_devolucao = CURRENT_DATE 
                WHERE id = %s;
            """, (id_emprestimo,))

            cur.execute("""
                INSERT INTO emprestimos_log (operacao, id_emprestimo, usuario_db)
                VALUES ('DEVOLVER', %s, %s)
            """, (id_emprestimo, DB_USER))

            self.conn.commit()
            cur.close()

            self.load_view()
            messagebox.showinfo("Sucesso", "Devolução registrada!")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao devolver:\n{e}")

    def delete_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um empréstimo.")
            return

        try:
            item = self.tree.item(selected[0])
            id_emprestimo = item["values"][0]

            cur = self.conn.cursor()
            cur.execute("DELETE FROM emprestimos WHERE id = %s;", (id_emprestimo,))

            cur.execute("""
                INSERT INTO emprestimos_log (operacao, id_emprestimo, usuario_db)
                VALUES ('EXCLUIR', %s, %s)
            """, (id_emprestimo, DB_USER))

            self.conn.commit()
            cur.close()

            self.load_view()
            messagebox.showinfo("Sucesso", "Empréstimo excluído!")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao excluir:\n{e}")

    # -------------------- LOGS --------------------
    def create_logs_tab(self):
        ttk.Label(self.tab_logs, text="Logs de Empréstimos", font=("Arial", 14, "bold")).pack(pady=10)

        self.tree_logs = ttk.Treeview(
            self.tab_logs,
            columns=("id_log", "op", "id_emprestimo", "usuario", "quando"),
            show="headings"
        )

        self.tree_logs.heading("id_log", text="ID Log")
        self.tree_logs.heading("op", text="Operação")
        self.tree_logs.heading("id_emprestimo", text="ID Empréstimo")
        self.tree_logs.heading("usuario", text="Usuário")
        self.tree_logs.heading("quando", text="Data/Hora")

        self.tree_logs.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(self.tab_logs, text="🔄 Atualizar Logs", command=self.load_logs).pack(pady=5)

        self.load_logs()

    def load_logs(self):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("""
                SELECT id_log, operacao, id_emprestimo, usuario_db, quando
                FROM emprestimos_log
                ORDER BY id_log DESC
                LIMIT 500;
            """)
            rows = cur.fetchall()
            cur.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar logs: {e}")
            return

        for item in self.tree_logs.get_children():
            self.tree_logs.delete(item)

        for row in rows:
            self.tree_logs.insert("", "end", values=(
                row["id_log"],
                row["operacao"],
                row["id_emprestimo"],
                row["usuario_db"],
                str(row["quando"])
            ))


# -------------------- TELA DE LOGIN --------------------
def login_screen():
    login = tk.Tk()
    login.title("Login - Biblioteca")
    login.geometry("320x200")
    login.resizable(False, False)

    tk.Label(login, text="Usuário:").pack(pady=(20, 5))
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Senha:").pack(pady=(10, 5))
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
            conn = get_connection()
            conn.close()
            login.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar:\n{e}")

    tk.Button(login, text="Entrar", width=15, command=autenticar).pack(pady=15)
    login.bind("<Return>", lambda e: autenticar())
    login.mainloop()


# -------------------- EXECUÇÃO PRINCIPAL --------------------
if __name__ == "__main__":
    print("🔐 Abrindo tela de login...")
    login_screen()

    if not DB_USER:
        print("❌ Login cancelado.")
    else:
        print(f"✅ Usuário autenticado: {DB_USER}")
        app = BibliotecaApp()
        app.mainloop()
