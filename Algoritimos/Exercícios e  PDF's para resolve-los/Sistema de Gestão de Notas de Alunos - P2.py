# Um professor deseja desenvolver um sistema para gerenciar as notas dos alunos de sua turma. 
# Esse  sistema  deve  permitir  cadastrar  alunos,  registrar  suas  notas  e  calcular  a  média  da  turma. 
# Além disso, o sistema precisa salvar essas informações em um arquivo e ser capaz de lidar com 
# possíveis erros de entrada e saída. Siga os requisitos abaixo para implementar a solução

import os

def adicionar_alunos(nome, notas, media, lista_de_alunos):
       
    dicionario_alunos = {
        "nome": nome,
        "notas": notas,
        "media": media,
    }

    lista_de_alunos.append(dicionario_alunos)

    print("aluno:",dicionario_alunos["nome"], "Adicionado com sucesso!")

def salvar_em_arquivo(lista_de_alunos):
    
    if os.path.exists("Alunos.txt"):
        resposta = input("Arquivo Alunos.txt ja existe, deseja subscreve-lo: (sim/nao) ")
        if resposta.lower() != "sim":
            print("Digite corretamente")
            return
    
    try:
        with open("Alunos.txt", "w") as Arquivo:
            for aluno in lista_de_alunos:
                nome = aluno["nome"]
                media = aluno["media"]
                Arquivo.write(f"Nome: {nome}, Media: {media:.2f} \n")
            print("Arquivo Alunos.txt Salvo com Sucesso!")
            
    except IOError as e:
        print("Erro ao salvar o arquivo {e}")
    
def ordenar_alunos(lista_de_alunos):
     for i in range(1, len(lista_de_alunos)):
        key = lista_de_alunos[i]
        j = i - 1
        while j >= 0 and key["media"] > lista_de_alunos[j]["media"]:
            lista_de_alunos[j + 1] = lista_de_alunos[j]
            j -= 1
        lista_de_alunos[j + 1] = key

def main():
    
    lista_de_alunos = []
    
    while True:
        print("\nOpções: \n1. Adicionar aluno \n2. Salvar em Arquivo \n3. Ordenar alunos por Media \n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            quantidade_notas = int(input("Digite a quantidade de Notas: "))
            if quantidade_notas < 2 or quantidade_notas > 5:
                print("Quantidade inválida")
            else:
                nome = input("Digite o nome do aluno: ")
                for i in range(quantidade_notas):
                    notas = float(input("Digite as notas consecutivamente: "))
                    media = (notas + notas) / quantidade_notas
                adicionar_alunos(nome, notas, media, lista_de_alunos)
        
        elif opcao == '2':
            salvar_em_arquivo(lista_de_alunos)
        
        elif opcao == '3':
            ordenar_alunos(lista_de_alunos)
            print("Os alunos foram ordenados por média!!")    
        
        elif opcao == '4':
            print("Saindo....")
            break
        
        else:
            print("Opção inválida, Digite novamente") 
main()
            