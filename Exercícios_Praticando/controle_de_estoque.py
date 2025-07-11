estoque = []


def adicionar_produto(nome_produto, quantidade):
    if quantidade <= 0:
        print("\nERRO: A quantidade deve ser um número positivo.")
        return

    for produto in estoque:
        if produto["nome_produto"] == nome_produto:
            produto["quantidade"] += quantidade
            print(f"\nEstoque de '{nome_produto}' atualizado para {produto['quantidade']} unidades.")
            return

    dic_estoque = {
        "nome_produto": nome_produto,
        "quantidade": quantidade
    }
    estoque.append(dic_estoque)
    print(f"\nProduto '{nome_produto}' ({quantidade} unidades) adicionado com sucesso!")


def remover_produto(nome_produto, quantidade):
    if not estoque:
        print("\nEstoque vazio!")
        return

    produto_encontrado = False
    for produto in estoque:
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


def listar_produtos():
    if not estoque:
        print("\nO estoque está vazio!")
        return

    print("\n--- LISTA DE ESTOQUE ---")
    for p in estoque:
        print(f"Produto: {p['nome_produto']} | Quantidade: {p['quantidade']}")
    print("------------------------\n")


def menu():
    while True:
        print("\nBem-vindo ao Sistema de Estoque")
        print("1: Adicionar Produto")
        print("2: Remover Quantidade de um Produto")
        print("3: Listar Produtos")
        print("4: Sair")

        try:
            opcao_str = input("Digite o número da opção desejada: ")
            if not opcao_str.isdigit():
                print("\nERRO: Por favor, digite um número válido.")
                continue
            
            opcao = int(opcao_str)

            if opcao == 1:
                try:
                    nome_produto = input("Digite o nome do produto: ").strip().upper()
                    if not nome_produto:
                        print("\nERRO: O nome do produto não pode ser vazio.")
                        continue

                    quantidade = int(input(f"Insira a quantidade de '{nome_produto}': "))
                    adicionar_produto(nome_produto, quantidade)
                
                except ValueError:
                    print("\nERRO: Quantidade inválida. Por favor, digite um número.")

            elif opcao == 2:
                try:
                    nome_produto = input("Digite o nome do produto: ").strip().upper()
                    if not nome_produto:
                        print("\nERRO: O nome do produto não pode ser vazio.")
                        continue
                        
                    quantidade = int(input(f"Insira a quantidade a ser removida de '{nome_produto}': "))
                    remover_produto(nome_produto, quantidade)

                except ValueError:
                    print("\nERRO: Quantidade inválida. Por favor, digite um número.")

            elif opcao == 3:
                listar_produtos()

            elif opcao == 4:
                print("\nSaindo do sistema...")
                break

            else:
                print("\nERRO: Opção inválida. Escolha um número do menu.")

        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
if __name__ == "__main__":
    menu()