class Estudante:
    #definindo o método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []
    
    #Adicionando as notas dos alunos
    def adicionar_notas(self, nota):
        self.notas.append(nota)
    
    #Mostrando a média das notas
    def pegar_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    #Mostra se o aluno esta com mais de 60% na nota de 100
    @property
    def passando(self):
        return self.pegar_media() >= 60
    
    #Método que chama os outros métodos
    @classmethod
    def main(cls):
        #lista de Estudantes
        estudantes = []

        while True:
            print('-' * 100)
            print("1 - Adicionar aluno")
            print("2 - Adionar nota")
            print("3 - Verificar aprovação")
            print("4 - Lista de Alunos Cadastrados")
            print("5 - Sair")
            print('-' * 100)

            escolha = int(input("Escolha uma das opções com base no seu respectivo dígito: "))

            if escolha == 1:
                nome = input("Nome do Aluno: ").lower()
                idade = int(input("Idade do Aluno: "))

                estudante = cls(nome, idade)

                estudantes.append(estudante)

                print("Aluno adicionado com sucesso !!!")
            
            #Cadastro de notas de alunos
            elif escolha == 2:
                #Verificação se existe objeto definido na lista de Estudantes
                if not estudantes:
                    print("Nenhum aluno cadastrado !!!")
                    #Se a lista for vazia, volta para o menu
                    continue
                #Iteração que forma um índice de alunos na listade Estudantes
                for idx, estudante in enumerate(estudantes):
                    print(f"{idx + 1} - {estudante.nome}")
                #Oção de escolher o indice do aluno
                estudante_idx = int(input("Escolha o número do Aluno: ")) - 1

                #verifica se o índice é válido
                if 0 <= estudante_idx < len(estudantes):
                    #Define a nota do Aluno
                    nota = float(input("Insira a Nota do Aluno: "))
                    #Escolhendo o objeto na lista e inserindo a nota nesse objeto
                    estudantes[estudante_idx].adicionar_notas(nota)
                    print("Nota adicionada!!")

                else:
                    print("Índice de Aluno inválido.")

            elif escolha == 3:
                if not estudantes:
                    print("Nenhum aluno Cadastrado!!!")
                    continue
                for estudante in estudantes:
                    nota_media = estudante.pegar_media()
                    if nota_media >= 6.0:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"
                    print('-' * 100)
                    print(f"""
                        - Nome do Estudante {estudante.nome}
                        - Média: {nota_media}
                        - Status: {status}
                          """)
                    print('-' * 100)

            #Inserir uma opção de listar os alunos cadastrados
             #Precisa mostrar:
                #nome dos alunos
                #idade
                #Lista das notas

            elif escolha == 4:
                if not estudante:
                    print("Nenhum aluno cadastrado!!")
                    continue
                else:
                    for est in estudantes:
                        print('-' * 100)
                        print(f"""
                        - Nome do Estudante: {est.nome}
                        - Idade: {est.idade}
                        - Notas: {est.notas}                       
                          """)
                        print('-' * 100)
            elif escolha == 5:
                print("Saindo......")
                print("Obrigado por usar nosso sistema")
                print("Até a próxima ;)")
                break

            else:
                print("Opção inválida. Tente novamente, se atente ao número relacionado a opção")

student = Estudante.main()