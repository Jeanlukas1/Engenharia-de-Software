class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        self.marcha = 0
    
    # Método de Apresentação
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
    
    # Método de Instância
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
            if self.marcha == 1:
                self.velocidade += 5
            elif self.marcha == 2:
                self.velocidade += 10
            elif self.marcha == 3:
                self.velocidade += 15
            elif self.marcha == 4:
                self.velocidade += 20
            elif self.marcha == 5:
                self.velocidade += 25
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} está desligado. Ligue o carro primeiro")
    
    def freiar(self):
        if self.is_running and self.velocidade > 0:
            self.velocidade -= 5
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} esta desligado ou sua velocidade ja é 0 km/h")
    
    def dar_re(self):
        if self.velocidade <= 1:
            self.marcha = -1
            print("O carro está dando ré.")
        else:
            print("Reduza a velocidade para dar ré.")
    
    def desligar(self):
        if self.velocidade > 0:
            while self.velocidade > 0:
                self.velocidade -= 5
                print(f"Reduzindo velocidade: {self.velocidade} km/h")
        self.is_running = False
        print("Carro desligado.")

                    