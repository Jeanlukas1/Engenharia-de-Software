# Um professor deseja desenvolver um sistema para gerenciar as notas dos alunos de sua turma. 
# Esse  sistema  deve  permitir  cadastrar  alunos,  registrar  suas  notas  e  calcular  a  média  da  turma. 
# Além disso, o sistema precisa salvar essas informações em um arquivo e ser capaz de lidar com 
# possíveis erros de entrada e saída. Siga os requisitos abaixo para implementar a solução

lista_de_alunos = []

def adicionar_alunos(nome, notas, media, lista_de_alunos):
       
    dicionario_alunos = {
        "nome": nome,
        "notas": notas,
        "media": media,
    }

    lista_de_alunos.append(dicionario_alunos)

    print("aluno:",dicionario_alunos["nome"], "Adicionado com sucesso!")

def salvar_em_arquivo(lista_de_alunos):
    with open("Alunos.txt", "") as Arquivo:
        Arquivo.write(lista_de_alunos)

def main():
    while True:
        print("\nOpções: \n1. Adicionar aluno \n2. Salvar em Arquivo \n3. Sair")
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
        
        else:
            break 
main()
            