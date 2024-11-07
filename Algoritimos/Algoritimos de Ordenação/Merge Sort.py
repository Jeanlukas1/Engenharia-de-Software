# Merge Sort

# Descrição: O Merge Sort é um algoritmo de ordenação baseado na técnica de divisão e conquista. 
# Ele divide a lista em duas metades, ordena cada metade recursivamente e, em seguida, 
# combina as duas metades ordenadas.

# Implementação:
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Vantagens:

# Estável
# Complexidade O(n log n)
# Eficiente para listas grandes

# Desvantagens:

# Utiliza espaço adicional (O(n))
# Pode ser mais lento em listas pequenas comparado a algoritmos mais simples