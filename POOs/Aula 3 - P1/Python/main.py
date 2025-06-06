#Gasta mais memória: 
#import Carro as Car

#Gasta menos memoria:
from Carro import Carro as Car

carro1 = Car("Fiat", "Uno com escada em cima", 2009, "Branco", "XTS85GH")
carro2 = Car("Uno", "Bolinha", 2004, "Preto", "XDFDA23")

#Usando o cadastro de vendas
#

print(carro1, "\n", carro2)

carro2.ligar_carro()

for i in range(4):
    carro2.acelerar()
    
for i in range(6):
    carro2.freiar()