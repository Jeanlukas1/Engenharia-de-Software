#include <stdio.h>
#include <stdlib.h>

int main (void){
    //Numeros inteiros: 1 2 3 4
    //Marcadores de posicão: %d

    //Numeros float: 1.2 3.4 ....
    //Marcadores de posição: %f

    //Gerando uma mensagem que imprima que o numero dois é um numero inteiro
    printf("\nO numero %d e um numero inteiro\n", 10);
    printf("\nO numero %1.1f e um nuemero decimal/float\n", 1.3);

    //Operadores aritimeticos Básicos
    // Soma: +
    // Divisao: /
    // Multiplicação: *
    // Subtração: -

    printf("\nA soma de 5 + 2 = %d \n", 5+2);
    //pra funcionar precisa por um ponto flutuante tambem na operação, por que eu estou mostrando que o resultado é uma fração entao por isso na operação precisa ter uma fração tambem
    printf("\nA Divisao de 5 / 2 = %f\n", 5 / 2.0);
    printf("\nA Subtração de 8 - 9 = %d\n", 8 - 9);
    printf("\nA Multiplicacao de 34 x 8 = %d\n", 34 * 8);

    printf("\n--------------------------------------------------------------------------------------------------\n");
    printf("\nExercicios\n");

    printf("\n1) Imprima a seguinte mensagem de texto: \n \n   'Eu quero ser um aluno nota 10'\n");
    printf("\nResolucao exercicio 1:\n \nEu quero ser um aluno nota %d\n", 10);

    printf("\n2) Maria Tem 40 anos e Joao tem 52, mostre na tela a soma da idade deles\n");
    printf("\nResolucao exercicio 2: A soma das idades de Maria e Joao e : %d\n", 40 + 52);

    printf("\n3) Marcelo comprou 5 tomates, cada um custou 2.3 reais, quanto ele gastou?\n");
    printf("\nResolucao exercicio 3: Marcelo gastou %1.1fR$ pagando 2.3R$ em 5 tomates\n", 2.3 * 5);

    printf("\n4) Joana comprou 23 caixas de leite e gastou no total 57.5 reais. Qual e o preço da caixa de leite?\n");
    printf("\nResoluçao exercicio 4: Se Joana comprou 23 caixas de leite e o valor total foi de 57.5R$, portanto o preco de cada caixa de leite foi de %1.2fR$\n", 57.5 / 23);
    return 0;
}
