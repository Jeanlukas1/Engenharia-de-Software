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
    
def listar_projetos():
    for projeto in projetos:
        print(f"Projeto: {projeto}") 
    return
print("Nenhum projeto encontrado!")
    
def teste():
    cadastrar_projeto("P001", "Cliente  A", "Gerente  X", "2024-01-01", "Planejamento") 
    cadastrar_projeto("P002", "Cliente  B", "Gerente  Y", "2024-02-01", "Em Andamento")
    cadastrar_projeto("P003", "Cliente A", "Gerente X", "2024-03-01", "Concluído")

    listar_projetos()
teste()

