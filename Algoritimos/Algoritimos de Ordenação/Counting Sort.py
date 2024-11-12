# Countig Sort

# Descrição: O Counting Sort é um algoritmo de ordenação que conta o número de ocorrências de cada valor distinto 
# em uma lista e usa essas contagens para determinar as posições dos valores na lista ordenada.

# Vantagens:

# Muito eficiente para listas com valores limitados
# Complexidade O(n + k)

# Desvantagens:

# Ineficiente para listas com um grande intervalo de valores
# Não é um algoritmo de ordenação comparativa

# Implementação:
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

resultado = counting_sort([9, 45, 56, 2, 74, 2, 672, 6, 245, 7, 24, 65, 23])