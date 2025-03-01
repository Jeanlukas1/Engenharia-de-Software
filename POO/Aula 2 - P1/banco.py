#criar uma classe
class Banco:
    #método construtor
    def __init__(self, banco, agencia, conta, cliente, cpf):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.cliente = cliente
        self.cpf = cpf
        self.saldo = 0
        self.senha = None

    # Método de definição de Senha
    def definir_senha(self, new_senha):
        if self.senha == None:
            self.senha = new_senha
            print("Sua senha foi definida!")
        elif self.senha != None:
            decisao = input("Você já possui uma senha definida, Deseja mudar a senha mesmo assim?")
            if decisao == "sim":
                self.senha = new_senha
        else:
            print("Escolha errada!")

    # Método de apresetação
    def __str__(self):
        return f"""
        Aqui estão os Dados da sua Conta Sr(a) {self.cliente}
----------------------------------------------
Cliente {self.cliente} Cadastrado com sucesso!
Conta: {self.conta}
Agência: {self.agencia}
Banco: {self.banco}
---------------------------------------------- 
        """
    # Deposito
    def deposito(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo += valor
            print(f"""
        Deposito 
--------------------------------------------------------------------------------------
Saldo do cliente {self.cliente} atualizado com sucesso, no valor de R${float(valor)}.
--------------------------------------------------------------------------------------
""")
    # Saque
    def saque(self, senha, valor):
        if self.senha == senha and self.saldo >= valor and isinstance(valor, (int, float)):
            self.saldo -= valor
            print(f"""
        Saque realizado pelo cliente {self.cliente}
-------------------------------------------
Saque realizado no valor de: {float(valor)}
-------------------------------------------
""")
        else:
            print("Valor ou senha incorreta, Tente novamente!")
    # Pix
    def pix(self, destinatario, valor):
        if isinstance(valor, (int, float)) and self.saldo >= valor:
            self.saldo -= valor
            destinatario.saldo += valor
            print(f"""
        Área Pix do cliente {self.cliente}
------------------------------------
Pix realizado no valor de R${valor}
De: {self.cliente}
Para: {destinatario.cliente}
------------------------------------
                  """)
    # caixinha
    # Extrato
    def extrato(self):
        print(
            f"""
        Extrato da conta {self.cliente}
--------------------------------------------
Conta: {self.conta}
Agência: {self.agencia}
Saldo: {self.saldo}
Cliente: {self.cliente}
--------------------------------------------
            """
        )

    