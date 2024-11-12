# Bucket Sort

# Descrição: O Bucket Sort distribui os elementos de uma lista em vários "baldes" (buckets) e, em seguida, 
# ordena cada balde individualmente usando outro algoritmo de ordenação ou recursivamente aplicando o Bucket Sort.

# Vantagens:

# Muito eficiente para listas uniformemente distribuídas
# Complexidade O(n + k)

# Desvantagens:

# Ineficiente se os dados não forem uniformemente distribuídos
# Desempenho depende da estratégia de distribuição dos buckets

# Implementação:
def bucket_sort(arr):
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)

    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

resultado = bucket_sort([9, 8, 6, 3, 432, 243, 234 ,123, 4353, 456, 32, 1])
print(resultado)