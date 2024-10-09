
lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        id = max(tarefa['id'] for tarefa in lista_tarefas) + 1    
    else:
        id = 1
    nova_tarefa = {
        

        "id" : id,
        "descricao" : descricao,
        "status" : status,
        "prioridade" : prioridade

    }

    lista_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in lista_tarefas:
            print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")


def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if (status is None or tarefa['status'] == status) and (prioridade is None or tarefa['prioridade'] == prioridade):
            tarefas_filtradas.append(tarefa)
    return tarefas_filtradas



def menu():
    tarefas_filtradas = []
    lista_tarefas = []
    while True:
        print("Digite o número correspondente as opções abaixo:")
        print("1 - Adicionar Tarefas")
        print("2 - Visualizar todas as tarefas")
        print("3 - Pesquise a sua tarefa com base no Status e na sua Prioridade")
        print("4 - Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == '1':
            descricao = input("Digite a descrição desta tarefa: ")
            status = input("Digite qual o status desta tarefa em: 'em andamento', 'pendente', 'concluída'")
            prioridade = input("Digite qual a prioridade desta tarefa: 'alta', 'média', 'baixa'")
            adicionar_tarefa(lista_tarefas, descricao, status, prioridade)
        
        elif opcao == '2':
            visualizar_tarefas(lista_tarefas)
        
        elif opcao == '3':
            status = input("Digite o Status da Tarefa em que procura: 'em andamento', 'pendente', 'concluída' ")
            prioridade = input("Digite o Prioridade da tarefa que procura: 'alta', 'média', 'baixa' ")
            tarefas_filtradas = filtrar_tarefas(lista_tarefas, status if status else None, prioridade if prioridade else None)
            visualizar_tarefas(tarefas_filtradas)
            
        elif opcao == '4':
            print("Saindo....")
            break
        
menu()                   
    