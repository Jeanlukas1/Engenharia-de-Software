
estoque = []


def adicionar_produto(nome_produto, quantidade=0):
    dic_estoque = {
        "nome_produto": nome_produto,
        "quantidade": quantidade
    }

    estoque.append(dic_estoque)

    print(
        f"Produto: {dic_estoque["nome_produto"]} | Quantidade: {dic_estoque["quantidade"]}, Adicionado ao estoque!")


def remover_produto(nome_produto, quantidade):
    if not estoque:
        print(f"Estoque vazio!")
        return
    for i in estoque:
        if i["nome_produto"] == nome_produto:
            i["quantidade"] -= quantidade
            if i["quantidade"] < 0:
                print("Quantidade inválida, produto ja esgotado")
                return
            print(f"""
        Estoque atualizado:
        
        {nome_produto}: {i["quantidade"]}  
        """)
        else:
            print("Nome não encontrado na lista de estoque!")


def listar_produtos():
    if not estoque:
        print("Estoque vazio!")
        return

    for p in estoque:
        print(f"""
        {p["nome_produto"]}: {p["quantidade"]} |
        """)


def menu():
    while True:
        print("Bem Vindo ao Nosso Sistema De Estoque")
        print("""
            Opção 1 : Adicionar Produto ao estoque
            Opção 2 : Remover Quantidade de um certo produto
            Opção 3 : Listar Produtos
            Opção 4 : Sair  
            """)

        try:
            opcao = int(input("Digite o número da respectiva opção: "))

            if opcao == 1:
                try:
                    nome_produto = input(
                        "Digite o Nome do produto a ser adicionado ao estoque: ")
                    quantidade = int(
                        input(f"Insira a quantidade de {nome_produto} a ser adicionado ao estoque: "))

                    adicionar_produto(nome_produto, quantidade)
                except ValueError:
                    print(
                        f"Adicione um nome e quantidade válida ao estoque: {ValueError}")

            if opcao == 2:
                nome_produto = input("Digite o nome do produto: ")
                quantidade = int(input(
                    f"Insira a quantidade que deseja retirar do estoque do(a) {nome_produto}: "))

                remover_produto(nome_produto, quantidade)
                
            if opcao == 3:
                listar_produtos()
                
            if opcao == 4:
                print("Saindo....")
                break
            
            else:
                print("Por favor escolha um número presente no menu de opções.")

        except ValueError:
            print(f"Número invalido: {ValueError}")


menu()
