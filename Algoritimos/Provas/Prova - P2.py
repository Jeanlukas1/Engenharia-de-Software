# Cada 
# obra possui informações detalhadas, como título, data de criação, tema, estilo artístico, 
# descrição, técnica utilizada, autor e localização na sala de exposição.

import os

lista_de_artistas = []

lista_de_obras = []

def adicionar_obra(id, titulo, data_de_criacao, tema, estilo_artistico, descricao, tecnica_utilizada, autor, localizacao):
    obra = {
        "id" : id,
        "titulo" : titulo,
        "data_de_criacao" : data_de_criacao,
        "tema" : tema,
        "estilo_artistico" : estilo_artistico,
        "descricao" : descricao,
        "tecnica_utilizada" : tecnica_utilizada,
        "autor" : autor,
        "localizacao" : localizacao
    }
    print(f"Obra com titulo: {obra["titulo"]} \nData de Criação: {obra["data_de_criacao"]} \nTema: {obra["tema"]} \nEstilo Artístico: {obra["estilo_artistico"]} \nDescrição: {obra["estilo_artistico"]} \nTécnica Utilizada: {obra["tecnica_utilizada"]} \nAutor: {obra["autor"]} \nLocalização: {obra["localizacao"]}")
    print("Adicionada ao Acervo!!!")
    lista_de_obras.append(obra)

def adicionar_artista(nome, data_de_nascimento, local_de_nascimento, biografia, estilos_artisticos, lista_de_obras):
    artista = {
        "nome" : nome,
        "data_de_nascimento" : data_de_nascimento,
        "local_de_nascimento" : local_de_nascimento,
        "biografia" : biografia,
        "estilos_artisticos" : estilos_artisticos
    }
    print(f"Artista {artista["nome"]} foi cadastrado a lista de artistas!!")
    if artista["nome"] in lista_de_artistas:
        print(f"{nome} Bem vindo!!")
        for i in lista_de_obras:
            print(i["autor"])
        return
    lista_de_artistas.append(artista)

def listagem_de_artistas(lista_de_artistas):
    if listagem_de_artistas == []:
        print("Lista Vazia")
    else:
        for artistas in lista_de_artistas:
            print(f"Artista {artistas + 1} - Nome: {artistas["nome"]} \nData de Nascimento: {artistas["data_de_nascimento"]} \nLocal de Nascimento: {artistas["local_de_nascimento"]} \nBiografia: {artistas["biografia"]} \nEstilo Artístico: {artistas["estilos_artistico"]}")

def listagem_de_obras(lista_de_obras):
    for obra in lista_de_obras:
        print(f"Obra {obra["id"]} - Título: {obra["titulo"]} \nData de Criação: {obra["data_de_criacao"]} \nTema: \nTema: {obra["tema"]} \nEstilo Artístico: {obra["estilo_artistico"]} \nDescrição: {obra["estilo_artistico"]} \nTécnica Utilizada: {obra["tecnica_utilizada"]} \nAutor: {obra["autor"]} \nLocalização: {obra["localizacao"]}")

def ordenar_obras(lista_de_obras):
     for i in range(1, len(lista_de_obras)):
        key = lista_de_obras[i]
        j = i - 1
        while j >= 0 and key["id"] < lista_de_obras[j]["id"]:
            lista_de_obras[j + 1] = lista_de_obras[j]
            j -= 1
        lista_de_obras[j + 1] = key

def salvar_em_arquivo(lista_de_obras):
    if os.path.exists("Python_Artes.txt"):
        resposta = print("Arquivo ja existe. Deseja subscrevelo? (s/n)")
        if resposta.lower() != "s":
            print("Digite novamente")
            return
        
    try:
        with open("Python_Artes.txt", "w") as Arquivo:
            for obra in lista_de_obras:
                Arquivo.write(f"Obra {obra["id"]} - Título: {obra["titulo"]} \nData de Criação: {obra["data_de_criacao"]} \nTema: \nTema: {obra["tema"]} \nEstilo Artístico: {obra["estilo_artistico"]} \nDescrição: {obra["estilo_artistico"]} \nTécnica Utilizada: {obra["tecnica_utilizada"]} \nAutor: {obra["autor"]} \nLocalização: {obra["localizacao"]}")
            print("Arquivo Salvo com sucesso!")

    except IOError as e:
        print(f"Erro {e}")

def menu():
    while True:

        print("------ BEM VINDO AO PYTHON ARTES ------")
        
        escolha_inicial = input("Você é um visitante ou é um de nossos colaborados(artista/gestor)? \nDigite ('visitante') ou ('gestor'): ")
        
        if escolha_inicial.lower() != "i":
            print("Digite novamente, Siga o padrão de letras minúsculas. ex:. visitante")
        
        if escolha_inicial == "visitante":
            print("Olá visitante, como está? \nAqui estão as opções disponíveis para Você!! ")
            print("1 - Lista de Obras \n2 - Conheça mais sobre os artistas")
            
            escolha_visitante = int(input("Digite o numero de escolha: ex:. 1 "))
        
            if escolha_visitante == 1:
                ordenar_obras(lista_de_obras)
                print("As Obras estão ordenadas por ID")
                listagem_de_obras(lista_de_obras)

            elif escolha_visitante == 2:
                print("Esses são nossos artistas, conheça mais sobre!!")
                listagem_de_artistas(lista_de_artistas)


        elif escolha_inicial == "gestor":
            print("Olá gestor, Aqui estão as opções disponíveis")
            print("1 - Adicionar artista \n2 - Adicionar obra \n3 - Salvar em arquivo")

            escolha_gestor = int(input("Digite o numero de escolha: ex:. 1 "))
        
            if escolha_gestor == 1:
                nome = input("Adicione o nome do artista: ")
                data_de_nascimento = input("Adicione a data de nascimento do artista:")
                local_de_nascimento = input("Adicione o Local de nascimento do artista:")
                biografia = input("Adicione a biografia do artista:")
                estilos_artisticos = input("Adicione o estilo artistico do artista:")
                
                adicionar_artista(nome, data_de_nascimento, local_de_nascimento, biografia, estilos_artisticos, lista_de_obras)

            elif escolha_gestor == 2:
                id = input("Digite o ID da obra")
                titulo = input("Adicione o Titulo da Obra: ")
                data_de_criacao = input("Adicione a data de criação da Obra:")
                tema = input("Adicione o Tema da Obra:")
                estilo_artistico = input("Adicione o estilo artístico da Obra:")
                descricao = input("Adicione a descrição da Obra:")
                tecnica_utilizada = input("Adicione a técnica utilizada na Obra:")
                autor = input("Adicione o autor da Obra:")
                localizacao = input("Adicione a localização da Obra:")

                adicionar_obra(id, titulo, data_de_criacao, tema, estilo_artistico, descricao, tecnica_utilizada, autor, localizacao)

            elif escolha_gestor == 3:
                salvar_em_arquivo(lista_de_obras)
menu()

