class Estoque:
    
    def __init__(self, nome):
        self.estoque = []
        self.nome = nome
        
    def adicionar_produto(self, nome_produto, quantidade):
        if quantidade <= 0:
            print("\nERRO: A quantidade deve ser um número positivo.")
            return

        for produto in self.estoque:
            if produto["nome_produto"] == nome_produto:
                produto["quantidade"] += quantidade
                print(f"\nEstoque de '{nome_produto}' atualizado para {produto['quantidade']} unidades.")
                return

        dic_estoque = {
            "nome_produto": nome_produto,
            "quantidade": quantidade
        }
        self.estoque.append(dic_estoque)
        print(f"\nProduto '{nome_produto}' ({quantidade} unidades) adicionado com sucesso!")
        
    def remover_produto(self, nome_produto, quantidade):
        if not self.estoque:
            print("\nEstoque vazio!")
            return

        produto_encontrado = False
        for produto in self.estoque:
            if produto["nome_produto"] == nome_produto:
                produto_encontrado = True
                if produto["quantidade"] >= quantidade:
                    produto["quantidade"] -= quantidade
                    print(f"""
    Estoque atualizado:
    {nome_produto}: {produto['quantidade']} unidades restantes.
    """)
                else:
                    print(f"\nERRO: Impossível remover {quantidade} unidades. Apenas {produto['quantidade']} em estoque.")
                break
        if not produto_encontrado:
            print("\nERRO: Produto não encontrado no estoque!")
    
    def listar_produtos(self):
        if not self.estoque:
            print("\nO estoque está vazio!")
            return

        print("\n--- LISTA DE ESTOQUE ---")
        for p in self.estoque:
            print(f"Produto: {p['nome_produto']} | Quantidade: {p['quantidade']}")
        print("------------------------\n")
    
joao = Estoque("Jõao")

joao.adicionar_produto("Pao", 30)
joao.remover_produto("Pãzo", 5)
joao.listar_produtos()
