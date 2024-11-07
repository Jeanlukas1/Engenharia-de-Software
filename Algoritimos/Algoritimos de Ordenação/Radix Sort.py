# Radix Sort

# Descrição: O Radix Sort ordena números inteiros processando-os dígito a dígito a partir do dígito 
# menos significativo para o mais significativo, usando um algoritmo de ordenação estável como o 
# Counting Sort para cada dígito.

# Implementação:
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Vantagens:

# Muito eficiente para listas de inteiros com um pequeno intervalo de dígitos
# Complexidade O(nk) (onde k é o número de dígitos)

# Desvantagens:

# Não é adequado para ordenar tipos de dados mais complexos
# Requer espaço adicional