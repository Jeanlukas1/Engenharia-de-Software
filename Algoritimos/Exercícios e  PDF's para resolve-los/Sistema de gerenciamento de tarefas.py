
lista_tarefas = []

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
    lista_tarefas = []
    while True:
        print("Digite o número correspondente às opções abaixo:")
        print("1 - Adicionar Tarefas")
        print("2 - Visualizar todas as tarefas")
        print("3 - Pesquisar tarefas com base no Status e na Prioridade")
        print("4 - Concluir tarefa")
        print("5 - Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição desta tarefa: ")
            status = input("Digite qual o status desta tarefa: 'em andamento', 'pendente', 'concluída'")
            prioridade = input("Digite qual a prioridade desta tarefa: 'alta', 'média', 'baixa'")
            adicionar_tarefa(lista_tarefas, titulo, descricao, status, prioridade)
        
        elif opcao == '2':
            visualizar_tarefas(lista_tarefas)
        
        elif opcao == '3':
            status = input("Digite o Status da Tarefa que procura: 'em andamento', 'pendente', 'concluída' ")
            prioridade = input("Digite a Prioridade da tarefa que procura: 'alta', 'média', 'baixa' ")
            tarefas_filtradas = filtrar_tarefas(lista_tarefas, status if status else None, prioridade if prioridade else None)
            visualizar_tarefas(tarefas_filtradas)
        
        elif opcao == '4':
            titulo_tarefa = input("Digite o título da tarefa a ser concluída: ")
            concluir_tarefa(lista_tarefas, titulo_tarefa)
        
        elif opcao == '5':
            print("Saindo....")
            break

menu()
           
    