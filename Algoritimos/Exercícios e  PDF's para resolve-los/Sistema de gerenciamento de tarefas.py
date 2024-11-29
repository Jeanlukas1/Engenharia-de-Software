
usuarios = []

def cadastrar_usuario(usuarios, nome, email, senha):
    if usuarios:
        id = max(usuario['id'] for usuario in usuarios) + 1    
    else:
        id = 1
    novo_usuario = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def login_usuario(usuarios, email, senha):
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"Bem-vindo, {usuario['nome']}!")
            return usuario
    print("Email ou senha incorretos.")
    return None

# Funções já existentes (modificadas)
def adicionar_tarefa(lista_tarefas, titulo, descricao, status, prioridade):
    if lista_tarefas:
        id = max(tarefa['id'] for tarefa in lista_tarefas) + 1    
    else:
        id = 1
    nova_tarefa = {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade
    }
    lista_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in lista_tarefas:
            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if (status is None or tarefa['status'] == status) and (prioridade is None or tarefa['prioridade'] == prioridade):
            tarefas_filtradas.append(tarefa)
    return tarefas_filtradas

def concluir_tarefa(lista_tarefas, titulo_tarefa):
    for tarefa in lista_tarefas:
        if tarefa['titulo'].lower() == titulo_tarefa.lower():
            tarefa['status'] = 'concluída'
            print(f"Tarefa '{titulo_tarefa}' concluída com sucesso!")
            return
    print(f"Tarefa '{titulo_tarefa}' não encontrada.")

def menu():
    usuarios = []
    lista_tarefas = []
    usuario_logado = None
    
    while True:
        print("Digite o número correspondente às opções abaixo:")
        print("1 - Cadastrar Usuário")
        print("2 - Login")
        print("3 - Adicionar Tarefas")
        print("4 - Visualizar todas as tarefas")
        print("5 - Pesquisar tarefas com base no Status e na Prioridade")
        print("6 - Concluir tarefa")
        print("7 - Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == '1':
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cadastrar_usuario(usuarios, nome, email, senha)
        
        elif opcao == '2':
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            usuario_logado = login_usuario(usuarios, email, senha)
        
        elif opcao == '3':
            if usuario_logado:
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição desta tarefa: ")
                status = input("Digite qual o status desta tarefa: 'em andamento', 'pendente', 'concluída'")
                prioridade = input("Digite qual a prioridade desta tarefa: 'alta', 'média', 'baixa'")
                adicionar_tarefa(lista_tarefas, titulo, descricao, status, prioridade)
            else:
                print("Por favor, faça login primeiro.")
        
        elif opcao == '4':
            if usuario_logado:
                visualizar_tarefas(lista_tarefas)
            else:
                print("Por favor, faça login primeiro.")
        
        elif opcao == '5':
            if usuario_logado:
                status = input("Digite o Status da Tarefa que procura: 'em andamento', 'pendente', 'concluída' ")
                prioridade = input("Digite a Prioridade da tarefa que procura: 'alta', 'média', 'baixa' ")
                tarefas_filtradas = filtrar_tarefas(lista_tarefas, status if status else None, prioridade if prioridade else None)
                visualizar_tarefas(tarefas_filtradas)
            else:
                print("Por favor, faça login primeiro.")
        
        elif opcao == '6':
            if usuario_logado:
                titulo_tarefa = input("Digite o título da tarefa a ser concluída: ")
                concluir_tarefa(lista_tarefas, titulo_tarefa)
            else:
                print("Por favor, faça login primeiro.")
        
        elif opcao == '7':
            print("Saindo....")
            break

menu()

           
    