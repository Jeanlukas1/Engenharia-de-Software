from Interfone import Interfone

class InterfoneEmergencia(Interfone):
    def __init__(self, modelo, endereco, servico, telefone_servico):
        super().__init__(modelo, endereco)
        self.servico = servico
        self.telefone_servico = telefone_servico

    @classmethod
    def cadastro(cls):
        modelo = input('\n Modelo: ')
        endereco = input(' Endereco: ')
        servico = input(' Servico: ')
        telefone_servico = input(' Telefone do servico: ')
        return cls(modelo, endereco, servico, telefone_servico)

    def ligar_para_proprietario(self):
        print(f'\n Ligando para o "{self.servico}" no numero "{self.telefone_servico}", do endereco "{self.endereco}"...')

    def registrar_chamada(self):
        print(f'\n Chamada registrada as 14:35 ...\n Duracao: 00:02:15 ...')

    def __str__(self):
        return f'\n Modelo: {self.modelo}\n Endereco: {self.endereco}\n Servico: {self.servico}\n Telefone do servico: {self.telefone_servico}'
