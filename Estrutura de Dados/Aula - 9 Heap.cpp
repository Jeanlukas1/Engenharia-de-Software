#include <stdio.h>
#define MAX 100

typedef struct {
    int chave;
} Elemento;

void subir(Elemento T[], int i) {
    int j = i / 2;
    if (j >= 1) {
        if (T[i].chave > T[j].chave) {
            Elemento temp = T[i];
            T[i] = T[j];
            T[j] = temp;
            subir(T, j);
        }
    }
}

void descer(Elemento T[], int i, int n) {
    int j = 2 * i;
    while (j <= n) {
        if (j < n && T[j + 1].chave > T[j].chave) {
            j = j + 1;
        }
        if (T[i].chave < T[j].chave) {
            Elemento temp = T[i];
            T[i] = T[j];
            T[j] = temp;
            i = j;
            j = 2 * i;
        } else {
            break;
        }
    }
}

void construir_heap(Elemento T[], int n) {
    for (int i = n / 2; i >= 1; i--) {
        descer(T, i, n);
    }
}


void exibir_heap(Elemento T[], int n) {
    for (int i = 1; i <= n; i++) {
        printf("%d ", T[i].chave);
    }
    printf("\n");
}

int main() {
    Elemento heap[MAX];
    int n;

    printf("Quantos elementos deseja inserir? ");
    scanf("%d", &n);

    printf("Digite os %d elementos:\n", n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &heap[i]);
    }

    printf("\nHeap construída:\n");
    construir_heap(heap, n);
    exibir_heap(heap, n);

    return 0;
}
