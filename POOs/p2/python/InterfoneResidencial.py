from Interfone import Interfone

class InterfoneResidencial(Interfone):
    def __init__(self, modelo, endereco, nome_proprietario, telefone_proprietario):
        super().__init__(modelo, endereco)
        self.nome_proprietario = nome_proprietario
        self.telefone_proprietario = telefone_proprietario

    @classmethod
    def cadastro(cls):
        modelo = input('\n Modelo: ')
        endereco = input(' Endereco: ')
        nome_proprietario = input(' Nome do proprietario: ')
        telefone_proprietario = input(' Telefone do proprietario: ')
        return cls(modelo, endereco, nome_proprietario, telefone_proprietario)

    def ligar_para_proprietario(self):
        print(f'\n Ligando para o "{self.nome_proprietario}" no numero "{self.telefone_proprietario}", do endereco "{self.endereco}"...')

    def registrar_chamada(self):
        print(f'\n Chamada registrada as 14:35 ...\n Duracao: 00:02:15 ...')

    def __str__(self):
        return f'\n Modelo: {self.modelo}\n Endereco: {self.endereco}\n Nome do proprietario: {self.nome_proprietario}\n Telefone do proprietario: {self.telefone_proprietario}'
