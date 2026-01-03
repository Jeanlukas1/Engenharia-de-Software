def dobro(lista):
    dobrar = [x * 2 for x in lista if x * 2 > 10]
    
    return dobrar

print(dobro([1, 2, 3, 4, 5, 6, 7]))
