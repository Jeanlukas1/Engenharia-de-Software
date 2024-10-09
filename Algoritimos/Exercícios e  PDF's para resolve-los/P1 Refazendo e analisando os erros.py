projetos = []


def cadastrar_projeto(codigo_do_projeto, nome_do_cliente, nome_do_gerente, data_de_inicio, status):
    dic = {

        "codigo_do_projeto": codigo_do_projeto,
        "nome_do_cliente": nome_do_cliente,
        "nome_do_gerente": nome_do_gerente,
        "data_de_início": data_de_inicio,
        "status": status      

    }
    projetos.append(dic)
    print(f"Projeto cadastrado com o código: {codigo_do_projeto} e nome: {nome_do_cliente} - Cadastrado com sucesso!")
    
def buscar_projeto(codigo):
    for projeto in projetos:
        if projeto['codigo'] == codigo:
            return projeto
    print(f"Projeto {codigo} não encontrado.")
    
def listar_projetos(projetos):
    if not projetos:
        print("Não está na lista de projetos")
    else:
        for projeto in projetos:
            print(f"Codigo do Projeto: {projeto['codigo_do_projeto']}, Nome do cliente: {projeto['nome_do_cliente']}, Nome do Gerente: {projeto['nome_do_gerente']}, Status: {projeto['status']}")
print("Nenhum projeto encontrado!")
    
def teste():
    cadastrar_projeto("P001", "Cliente  A", "Gerente  X", "2024-01-01", "Planejamento") 
    cadastrar_projeto("P002", "Cliente  B", "Gerente  Y", "2024-02-01", "Em Andamento")
    cadastrar_projeto("P003", "Cliente A", "Gerente X", "2024-03-01", "Concluído")

    listar_projetos(projetos)
    
    buscar_projeto("P001")

teste()