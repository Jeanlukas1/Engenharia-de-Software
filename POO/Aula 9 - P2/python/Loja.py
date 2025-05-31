class Loja:
    def __init__(self):
        self.catalogo = []
        

    def adicionar_produto(self, produto, valor):
        catalogo = {
            "produto": produto,
            "valor": valor
        }
        self.catalogo.append(catalogo)
        print(f"|Produto: {catalogo["produto"]}, Valor: {catalogo["valor"]}, cadastrado!.|")
        print()
    
    def listar_produto(self):
        if not self.catalogo:
            print("Lista de produtos vazia!, adicione um produto primeiro.")
            return
        for i in self.catalogo:
            print(f"|Produto: {i["produto"]}, Valor: {i["valor"]}|")
            print()
    
    def remover_produto(self, produto):
        for i in self.catalogo:
            if i["produto"] == produto:
                self.catalogo.remove(i)
                print(f"|Produto '{produto}' removido com sucesso!|")
                return
        print(f"|Produto '{produto}' não encontrado no catálogo.|")

    def realizar_venda():
        pass
    def oferecer_promo():
        pass
    
class Conta:
    @classmethod
    def agencia(cls):
        return "6452-4"
    
    def __init__(self, nome_cliente, numero_conta):
        self.nome_cliente = nome_cliente 
        self.numero_conta = numero_conta
        self.cheque_especial = 0.0
        self.limite_cartao = 0.0
        self.__pix = None
        self.saldo = 0
        self.__senha = None

    def cadastrar(self, senha):
        print(f"Olá, {self.nome_cliente}! Bem vindo ao Nosso PyBank!")
        if self.__senha == None:
            self.__senha = senha
            print("Sua senha foi definida!")
        elif self.__senha != None:
            decisao = input("Você já possui uma senha definida, Deseja mudar a senha mesmo assim?")
            if decisao == "sim":
                self.__senha = senha
            print("Escolha errada!")
    
    def autenticar_senha(self, senha):
        if self.__senha != None and self.__senha == senha:
            print()


# pr1 = Loja()

# pr1.adicionar_produto("Bola de futebol", "100")
# pr1.adicionar_produto("Casaco", "150")
# pr1.adicionar_produto("Tênis", "140")
# print("-" *100)
# pr1.listar_produto()
# print("-" *100)
# pr1.remover_produto("Tênis")
# print("-" *100)
# pr1.listar_produto()
# print("-" *100)

c = Conta("Jean Lukas", "23132132131", "2000", "4000")

c.cadastrar("1907050603")

