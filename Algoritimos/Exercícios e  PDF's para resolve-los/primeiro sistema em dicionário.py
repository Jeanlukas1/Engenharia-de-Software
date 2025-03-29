clientes = {}
#adicionar
def adicionar_cliente(nome, email, telefone, endereco):
    if email in clientes:
        print(f"Cliente com e-mail {email} já existe.")
        return
    clientes[email] = {
        'nome': nome,
        'telefone': telefone,
        'endereco': endereco
    }
    print(f"Cliente {nome} adicionado com sucesso.")

def exibir_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("Lista de Clientes:")
    for email, info in clientes.items():
        print(f"Nome: {info['nome']}, E-mail: {email}, Telefone: {info['telefone']}, Endereço: {info['endereco']}")

def buscar_cliente(email):
    if email in clientes:
        info = clientes[email]
        print(f"Cliente encontrado: Nome: {info['nome']}, E-mail: {email}, Telefone: {info['telefone']}, Endereço: {info['endereco']}")
    else:
        print(f"Cliente com e-mail {email} não encontrado.")

def remover_cliente(email):
    if email in clientes:
        del clientes[email]
        print(f"Cliente com e-mail {email} removido com sucesso.")
    else:
        print(f"Cliente com e-mail {email} não encontrado.")

def menu():
    while True:
        print("--- Sistema de Gerenciamento de Clientes ---")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por E-mail")
        print("4. Remover Cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            adicionar_cliente(nome, email, telefone, endereco)
        
        elif opcao == '2':
            exibir_clientes()
        
        elif opcao == '3':
            email = input("Digite o e-mail do cliente para buscar: ")
            buscar_cliente(email)
        
        elif opcao == '4':
            email = input("Digite o e-mail do cliente para remover: ")
            remover_cliente(email)
        
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida, por favor escolha novamente.")

menu()
