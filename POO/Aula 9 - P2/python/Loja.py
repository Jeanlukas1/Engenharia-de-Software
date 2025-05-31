class Loja:
    def __init__(self):
        self.catalogo = []

    def adicionar_produto(self, produto, valor):
        catalogo = {
            "produto": produto,
            "valor": float(valor)
        }
        self.catalogo.append(catalogo)
        print(f"|Produto: {catalogo['produto']}, Valor: {catalogo['valor']}, cadastrado!.|")
        print()
    
    def listar_produto(self):
        if not self.catalogo:
            print("Lista de produtos vazia!, adicione um produto primeiro.")
            return
        for i in self.catalogo:
            print(f"|Produto: {i['produto']}, Valor: {i['valor']}|")
            print()
    
    def remover_produto(self, item_index):
        if 0 <= item_index < len(self.catalogo):
            return self.catalogo.pop(item_index)
        return None

    def realizar_venda(self):
        pass

    def oferecer_promo(self):
        pass


class Conta:
    AGENCIA = "6452-4"

    def __init__(self, nome_cliente, numero_conta):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.cheque_especial = 500.0
        self.limite_cartao = 1000.0
        self.__pix = None
        self.__senha = None
        self.__saldo = 0.0

    @classmethod
    def agencia(cls):
        return cls.AGENCIA

    def cadastrar(self, senha):
        print(f"Olá, {self.nome_cliente}! Bem-vindo ao Nosso PyBank!")
        if self.__senha is None:
            self.__senha = senha
            print("Sua senha foi definida com sucesso!")
        else:
            decisao = input("Você já possui uma senha definida. Deseja mudá-la mesmo assim? (sim/não): ").lower()
            if decisao == "sim":
                self.__senha = senha
                print("Senha alterada com sucesso!")
            else:
                print("Senha não foi alterada.")

    def autenticar_senha(self, senha):
        if self.__senha is not None and self.__senha == senha:
            print("Autenticação bem-sucedida!")
            return True
        print("Senha incorreta.")
        return False

    def cadastrar_pix(self, chave):
        if self.__pix is None:
            self.__pix = chave
            print("Chave PIX cadastrada com sucesso!")
        else:
            print("Você já possui uma chave PIX cadastrada.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor, senha):
        if not self.autenticar_senha(senha):
            return
        if 0 < valor <= (self.__saldo + self.cheque_especial):
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente (incluindo cheque especial).")

    def pix(self, valor, destino, senha):
        if not isinstance(destino, Conta):
            print("Conta de destino inválida.")
            return
        if not self.autenticar_senha(senha):
            return
        if valor <= 0 or valor > (self.__saldo + self.cheque_especial):
            print("Transferência inválida: valor excede o saldo.")
            return
        self.__saldo -= valor
        destino.__saldo += valor
        print(f"Transferência de R$ {valor:.2f} para {destino.nome_cliente} realizada com sucesso.")

    def exibir_dados(self):
        print(f"Cliente: {self.nome_cliente}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Agência: {self.agencia()}")
        print(f"Saldo: R$ {self.__saldo:.2f}")
        print(f"Cheque Especial: R$ {self.cheque_especial:.2f}")
        print(f"Limite do Cartão: R$ {self.limite_cartao:.2f}")
        print(f"Chave PIX: {self.__pix if self.__pix else 'Não cadastrada'}")


class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self._desconto = 0.0 
    
    def realizar_venda(self, metodo, conta, item_index, produto):
        item = self.remover_produto(item_index)
        if item and item["produto"] == produto:
            print("Venda realizada com", metodo)
            print("Produto:", produto)
            print("Desconto aplicado:", self._desconto * 100, "%")
        else:
            print("Erro: Produto não encontrado ou índice inválido.")

    def oferecer_promocao(self, desconto):
        self._desconto = desconto
        print("Promoção: desconto de", desconto * 100, "% aplicado.")


usr1 = Conta("Jean Lukas", "23132132131")
usr2 = Conta("Zé", "23132332132")

usr1.cadastrar("1907050603")
print()
print("-" *100)
print()
usr1.autenticar_senha("1907050603")
print()
print("-" *100)
print()
usr1.cadastrar_pix("178.558.307-74")
print()
print("-" *100)
print()
usr1.depositar(2000)
print()
print("-" *100)
print()
usr1.sacar(200, "1907050603")
print()
print("-" *100)
print()
usr1.pix(300, usr2, "1907050603")
print()
print("-" *100)
print()
usr2.cadastrar("1907050603")
print()
print("-" *100)
print()
usr2.autenticar_senha("1907050603")
print()
print("-" *100)
print()
usr2.cadastrar_pix("178.558.307-72")
print()
print("-" *100)
print()
usr1.exibir_dados()
print()
print("-" *100)
print()

usr3 = LojaFisica()
usr3.adicionar_produto("Bola de futebol", "100")
usr3.adicionar_produto("Casaco", "150")
usr3.adicionar_produto("Tênis", "140")
print()
print("-" *100)
print()
usr3.listar_produto()
print()
print("-" *100)
print()

print()
print("-" *100)
print()
usr3.realizar_venda("pix", usr1, 1, "Casaco")
print()
print("-" *100)
print()
