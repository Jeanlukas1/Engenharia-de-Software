#BUSCA SEQUENCIAL

chave = 14
lista = [11,12,13,14]

def busca_Sequencial(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
    return -1

x = busca_Sequencial(lista, chave)

if x != -1:
    print("Posição da chave", chave, "na lista:", x)
else:
    print("A chave", chave, "não se encontra na lista")

#BUSCA BINÁRIA

lista = [10,11,12,13]
lista.sort