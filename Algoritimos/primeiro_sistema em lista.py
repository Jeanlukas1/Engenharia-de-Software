# Adicionar Cliente: Implemente uma função chamada
# adicionar_cliente(nome, email, telefone, endereco) que adicione um
# novo cliente à lista clientes

clientes = []

def adicionar_cliente(nome, email, telefone, endereço):
    cliente = [nome, email, telefone, endereço]
    clientes.append(cliente)
    print(clientes)

adicionar_cliente('Jean', 'lukasjean745@gmail.com', 'telefone', 'jacone, rua 99')
adicionar_cliente('lukas', 'lukasjean745@gmail.com', 'telefone', 'jacone, rua 99')


#Exibir Clientes: Implemente uma função chamada exibir_clientes() que
#exiba todos os clientes cadastrados, listando suas informações.

def exibir_clientes():
    
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"E-mail: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Endereço: {cliente['endereco']}")
        


#Buscar Cliente por E-mail: Implemente uma função chamada
#buscar_cliente(email) que permita buscar um cliente pelo seu e-mail e exibir
#suas informações.

def buscar_cliente(email):
    for cliente in clientes:
        if cliente['email'] == email:
            print(f"Nome: {cliente['nome']}")
            print(f"E-mail: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Endereço: {cliente['endereco']}")
            return
    

#Remover Cliente: Implemente uma função chamada remover_cliente(email)
#que remova um cliente da lista com base no seu e-mail.


def remover_cliente(email):
    cliente = buscar_cliente(email)
    if cliente:
        clientes.remove(cliente)
        print(f"Cliente com o email {email} removido com sucesso!")
    

#Teste das Funcionalidades:
#o Crie um script principal que permita ao usuário interagir com o sistema,
#escolhendo entre adicionar, exibir, buscar ou remover clientes.
#o Teste o sistema adicionando, exibindo, buscando e removendo clientes.
    
def main():
    while True:
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por E-mail")
        print("4. Remover Cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif opcao == '2':
            exibir_clientes()
        elif opcao == '3':
            email = input("Digite o e-mail do cliente: ")
            buscar_cliente(email)
        elif opcao == '4':
            email = input("Digite o e-mail do cliente a ser removido: ")
            remover_cliente(email)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()
