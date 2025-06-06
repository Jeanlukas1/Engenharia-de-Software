# definindo o método construtor da classe
class Carro:
    # Método construtor
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        self.marcha = 0 # -1 é a marcha ré e 0 neutro
    
    # Método de apresentação
    # Método de classe
    def __str__(self):
        return f"""
O carro de Marca {self.marca} e modelo {self.modelo}
do ano {self.ano} e cor {self.cor} saiu da loja e hoje tem a placa
{self.placa}
            """
    
    # método de instância
    @classmethod
    def cadastro_venda(cls):
        marca = input("Digite aqui a marca do carro comprado: ")
        modelo = input("Digite aqui o modelo do carro comprado: ")
        ano = int(input("Digite aqui o ano do carro comprado: "))
        cor = input("Digite aqui a cor do carro comprado: ")
        placa = input("Digite aqui a placa do carro comprado: ")
        return cls(marca, modelo, ano, cor, placa)
    
    
    def ligar_carro(self):
        if not self.is_running:
            self.is_running = True
            print("O carro foi ligado..... RUMRUMRUMRUM")
        else:
            print("O carro já esta ligado!!!")
    
    def muda_marcha(self, re = False):
        if self.velocidade >=0 and self.velocidade <= 20 and not re:
            self.marcha = 1
        elif self.velocidade > 20 and self.velocidade <= 40:
            self.marcha = 2
        elif self.velocidade > 40 and self.velocidade <= 60:
            self.marcha = 3
        elif self.velocidade > 60 and self.velocidade <= 80:
            self.marcha = 4
        elif self.velocidade > 80 and self.velocidade <= 100:
            self.marcha = 5
        elif self.velocidade > 100:
            self.marcha = 6
            if self.velocidade > 120:
                self.velocidade = 120
        elif self.velocidade == 10 and re:
            self.marcha = -1
        elif self.velocidade == 0 and re:
            self.marcha = 0
    
    # montar um acelerador que ira acelerar com base na marchar definida
    # Considerando que seja um carro automatico
    def acelerar(self, re = False):
        if self.is_running and not re:
            self.velocidade += 5
            self.muda_marcha(re)
            print(f"Velocidade {self.velocidade} km/h e Marcha {self.marcha}")
        elif self.is_running and re:
            dicio = {0:"Neutro", -1:"Ré"}
            self.muda_marcha(re)
            self.velocidade = 10
            print(f"Velocidade {self.velocidade} km/h e Marcha {dicio[self.marcha]}")
        else:
            print(f"O carro {self.modelo} esta desligado precisa ligar o carro primeiro!!!")

    def freiar(self, re = False):
        if self.is_running and not re and self.velocidade >= 0:
            self.velocidade -= 5
            if self.velocidade < 0:
                self.velocidade = 0
            self.muda_marcha(re)
            print(f"Velocidade {self.velocidade} km/h e Marcha {self.marcha}")
        elif self.is_running and re and self.velocidade == 10:
            dicio = {0:"Neutro", -1:"Ré"}
            self.velocidade = 0
            self.muda_marcha(re)
            print(f"Velocidade {self.velocidade} km/h e Marcha {dicio[self.marcha]}")
        else:
            print(f"O carro {self.modelo} esta desligado precisa ligar o carro primeiro!!!")
