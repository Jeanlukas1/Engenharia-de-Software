import Carro as Car

carro1 = Car.Carro("Fiat", "Uno", 2007, "Branco", "PHTG0LK")

print(carro1)

carro1.ligar_carro()

for i in range(30):
    carro1.acelerar()

for i in range(30):
    carro1.freiar()

for i in range(5):
    carro1.acelerar(True)

