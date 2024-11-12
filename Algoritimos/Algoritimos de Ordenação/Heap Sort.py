# Heap Sort

# Descrição: O Heap Sort utiliza uma estrutura de dados chamada heap para ordenar os elementos. 
# Ele constrói um heap a partir da lista e depois remove o maior elemento repetidamente para construir 
# a lista ordenada.

# Vantagens:

# Complexidade O(n log n)
# Não requer espaço adicional significativo

# Desvantagens:

# Não é estável
# Pode ser mais lento que o Quick Sort na prática

# Implementação:
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

resultado = heap_sort([76, 234, 56, 13, 34, 5, 123, 3, 56, 13, 56, 234, 5, 1, 5, 67,])
print(resultado)

