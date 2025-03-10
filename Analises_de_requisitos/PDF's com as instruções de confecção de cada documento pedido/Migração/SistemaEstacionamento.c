#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VAGAS 100

typedef struct {
    int id;
    char placa[8];
    int ocupado;
} Vaga;

Vaga estacionamento[MAX_VAGAS];

void inicializarEstacionamento() {
    for (int i = 0; i < MAX_VAGAS; i++) {
        estacionamento[i].id = i + 1;
        estacionamento[i].ocupado = 0;
    }
}

void exibirVagas() {
    printf("Vagas disponíveis:\n");
    for (int i = 0; i < MAX_VAGAS; i++) {
        if (!estacionamento[i].ocupado) {
            printf("Vaga %d está livre.\n", estacionamento[i].id);
        }
    }
}

void estacionarVeiculo() {
    char placa[8];
    printf("Informe a placa do veículo: ");
    scanf("%s", placa);

    for (int i = 0; i < MAX_VAGAS; i++) {
        if (!estacionamento[i].ocupado) {
            estacionamento[i].ocupado = 1;
            strcpy(estacionamento[i].placa, placa);
            printf("Veículo com placa %s estacionado na vaga %d.\n", placa, estacionamento[i].id);
            return;
        }
    }
    printf("Estacionamento cheio!\n");
}

void removerVeiculo() {
    char placa[8];
    printf("Informe a placa do veículo a ser removido: ");
    scanf("%s", placa);

    for (int i = 0; i < MAX_VAGAS; i++) {
        if (estacionamento[i].ocupado && strcmp(estacionamento[i].placa, placa) == 0) {
            estacionamento[i].ocupado = 0;
            printf("Veículo com placa %s removido da vaga %d.\n", placa, estacionamento[i].id);
            return;
        }
    }
    printf("Veículo não encontrado.\n");
}

int main() {
    int opcao;
    inicializarEstacionamento();

    do {
        printf("\nSistema de Gerenciamento de Estacionamento\n");
        printf("1. Exibir Vagas\n");
        printf("2. Estacionar Veículo\n");
        printf("3. Remover Veículo\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                exibirVagas();
                break;
            case 2:
                estacionarVeiculo();
                break;
            case 3:
                removerVeiculo();
                break;
            case 4:
                printf("Saindo do sistema...\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 4);

    return 0;
}
