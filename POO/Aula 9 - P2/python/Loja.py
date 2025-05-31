class Loja:
    def __init__(self, nome):
        self.nome = nome
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
    
class 

pr1 = Loja("Jean Lukas")

pr1.adicionar_produto("Bola de futebol", "100")
pr1.adicionar_produto("Casaco", "150")
pr1.adicionar_produto("Tênis", "140")
print("-" *100)
pr1.listar_produto()
print("-" *100)
pr1.remover_produto("Tênis")
print("-" *100)
pr1.listar_produto()
print("-" *100)


