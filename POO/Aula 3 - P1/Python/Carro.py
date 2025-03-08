class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        
    #Método de Apresentação
    def __str__(self):
        return f"""
    O carro de: 
    Marca: {self.marca}
    Modelo: {self.modelo}
    Ano: {self.ano}
    Cor: {self.cor}
    Placa: {self.placa} 
    Saiu da loja hoje! 
    """
    #Método de Instância
    @classmethod
    def cadastro_venda(cls):
        marca = input("Digite aqui a marca do carro comprado: ")
        modelo = input("Digite aqui o modelo do carro comprado: ")
        ano = input("Digite aqui o ano do carro comprado: ")
        cor = input("Digite aqui o cor do carro comprado: ")
        placa = input("Digite aqui a placa do carro comprado: ")
        return cls(marca, modelo, ano, cor, placa)
        
    def ligar_carro(self):
        if not self.is_running:
            self.is_running = True
            print("O carro foi ligado.......... RUURRURURURM")
        else:
            print("O carro ja esta ligado!!")
            
    def acelerar(self):
        if self.is_running:
            self.velocidade += 5
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} está desligado. Ligue o carro primeiro")
    
    def freiar(self):
        if self.is_running and self.velocidade > 0:
            self.velocidade -= 5
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} esta desligado ou sua velocidade ja é 0 km/h")
                    