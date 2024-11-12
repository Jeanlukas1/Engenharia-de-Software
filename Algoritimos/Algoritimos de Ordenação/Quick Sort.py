# Quick Sort

# Descrição: O Quick Sort é um algoritmo de divisão e conquista que seleciona um "pivô" 
# e particiona a lista em duas partes, uma com elementos menores que o pivô e outra com elementos maiores, 
# e depois ordena cada parte recursivamente.

# Vantagens:

# Eficiente para listas grandes
# Complexidade média O(n log n)
# Não requer espaço adicional significativo

# Desvantagens:

# Complexidade pior caso O(n²) (se o pivô for escolhido mal)
# Não é estável

# Implementação:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
resultado = quick_sort([9, 6, 3, 7, 2, 6, 2, 43, 3, 5, 45, ])
print(resultado)

