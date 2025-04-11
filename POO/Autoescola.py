class Aluno():
    def __init__(self, nome, endereco, email, telefone) -> None:
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    def get_dados(self):
        return {
            'nome' : self.nome,
            'endereco' : self.endereco,
            'email' : self.email,
            'telefone' : self.telefone
        }

    def adicionar_aluno(self, alunos):
        aluno = self.get_dados()
        if aluno not in alunos:
            alunos.append(aluno)
            print('\n Aluno adicionado...')
        else:
            print('\n Aluno já existe...')

    def atualizar_dados(self, alunos):
        aluno = self.get_dados()

        print('\n ATUALIZAR DADOS DO ALUNO:\n')
        self.nome = input(' Nome: ')
        self.endereco = input(' Endereço: ')
        self.email = input(' E-mail: ')
        self.telefone = input(' Telefone: ')

        atualizado = self.get_dados()

        for i, cadastrado in enumerate(alunos):
            if aluno == cadastrado:
                alunos[i] = atualizado
                print('\n Dados atualizados...')

    def __str__(self) -> str:
        return f'\n Nome: {self.nome}\n Endereço: {self.endereco}\n E-mail: {self.email}\n Telefone: {self.telefone}'

class Curso():
    def __init__(self, nome, descricao, carga_horaria, vagas) -> None:
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria
        self.vagas = vagas
        self.inscritos = []
    
    def get_dados(self):
        return {
            'nome' : self.nome,
            'descricao' : self.descricao,
            'carga_horaria' : self.carga_horaria,
            'vagas' : self.vagas
        }
    
    def adicionar_curso(self, cursos):
        curso = self.get_dados()
        if curso not in cursos:
            cursos.append(curso)
            print('\n Aluno adicionado...')
        else:
            print('\n Aluno já existe...')

    def atualizar_dados(self, cursos):
        curso = self.get_dados()

        print('\n ATUALIZAR DADOS DO ALUNO:\n')
        self.nome = input(' Nome: ')
        self.descricao = input(' Descrição: ')
        self.carga_horaria = input(' Carga horária: ')
        self.vagas = input(' Vagas: ')

        atualizado = self.get_dados()

        for i, cadastrado in enumerate(cursos):
            if curso == cadastrado:
                cursos[i] = atualizado
                print('\n Dados atualizados...')

    def inscrever_aluno(self, aluno):
        if self.vagas > 0:
            inscrito = {
                'nome' : aluno.nome,
                'endereco' : aluno.endereco,
                'email' : aluno.email,
                'telefone' : aluno.telefone
            }
            self.inscritos.append(inscrito)
        else:
            print('\n Não a vagas !!!')

    def __str__(self) -> str:
        return f'\n Nome: {self.nome}\n Descrição: {self.descricao}\n Carga horária: {self.carga_horaria}\n Vagas: {self.vagas}'

    @classmethod
    def listar_cursos(cls, cursos):
        for curso in cursos:
            cls.nome = curso['nome']
            cls.descricao = curso['descricao']
            cls.carga_horaria = curso['carga_horaria']
            cls.vagas = curso['vagas']
            print(cls)

def main():
    alunos = []
    cursos = []
    
    aluno1 = Aluno('Leandro', 'Rua A', 'leandro@gmail.com', '99999999')
    aluno1.adicionar_aluno(alunos)
    aluno2 = Aluno('João', 'Rua C', 'joao@gmail.com', '88888888')
    aluno2.adicionar_aluno(alunos)
    aluno3 = Aluno('Luna', 'Rua B', 'luna@gmail.com', '99999999')
    aluno3.adicionar_aluno(alunos)
    aluno4 = Aluno('Mario', 'Rua C', 'mario@gmail.com', '88888888')
    aluno4.adicionar_aluno(alunos)

    curso1 = Curso('Carro', 'É um curso...', '300', 10)
    curso1.adicionar_curso(cursos)
    curso2 = Curso('Moto', 'É um curso...', '300', 5)
    curso2.adicionar_curso(cursos)

    curso1.inscrever_aluno(aluno1)
    curso1.inscrever_aluno(aluno2)
    curso2.inscrever_aluno(aluno3)
    curso2.inscrever_aluno(aluno4)

    print('-' * 100)
    print(curso1)
    print('-' * 100)
    for aluno in curso1.inscritos:
        print(f'\n Nome: {aluno['nome']}')
        print(f' Endereço: {aluno['endereco']}')
        print(f' E-mail: {aluno['email']}')
        print(f' Telefone: {aluno['telefone']}')

    print('-' * 100)
    print(curso2)
    print('-' * 100)
    for aluno in curso2.inscritos:
        print(f'\n Nome: {aluno['nome']}')
        print(f' Endereço: {aluno['endereco']}')
        print(f' E-mail: {aluno['email']}')
        print(f' Telefone: {aluno['telefone']}')
    print('-' * 100)

if __name__ == '__main__':
    main()
