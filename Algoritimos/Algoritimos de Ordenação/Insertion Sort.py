# Insertion Sort 

# Descrição: O Insertion Sort é um algoritmo simples que constrói a lista ordenada um elemento por vez, 
# retirando cada elemento da lista não ordenada e inserindo-o na posição correta na lista ordenada. 


# Vantagens: 

# Simples de implementar 
# Eficiente para pequenas listas ou listas quase ordenadas 
# Estável (não muda a ordem relativa de elementos iguais) 

# Desvantagens: 

# Ineficiente para listas grandes (complexidade O(n²)) 
# Não é adequado para listas que necessitam de desempenho rápido 

# Implementação:
    
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

