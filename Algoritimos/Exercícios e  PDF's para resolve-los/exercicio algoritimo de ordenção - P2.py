import random
import time

def gerar_lista_aleatoria(tamanho):
    return [random.randint(1, 1000000) for _ in range(tamanho)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocado = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocado = True
        if not trocado:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

tamanho = 10_000_000
lista_aleatoria_bubble = gerar_lista_aleatoria(tamanho)
lista_aleatoria_selection = lista_aleatoria_bubble.copy()

inicio_tempo = time.time()
bubble_sort(lista_aleatoria_bubble)
fim_tempo = time.time()
print(f"Bubble Sort levou {fim_tempo - inicio_tempo:.2f} segundos.")

inicio_tempo = time.time()
selection_sort(lista_aleatoria_selection)
fim_tempo = time.time()
print(f"Selection Sort levou {fim_tempo - inicio_tempo:.2f} segundos.")

