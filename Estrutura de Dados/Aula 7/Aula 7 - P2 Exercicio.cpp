#include <iostream>
using namespace std;

// Implementação simples de deque usando array
class Deque {
private:
    char data[100]; // Tamanho máximo de 100 caracteres
    int front;
    int rear;

public:
    Deque() {
        front = -1;
        rear = -1;
    }

    bool isEmpty() {
        return front == -1;
    }

    void pushBack(char c) {
        if (rear == 99) {
            cout << "Deque cheio!" << endl;
            return;
        }
        if (isEmpty()) {
            front = rear = 0;
        } else {
            rear++;
        }
        data[rear] = c;
    }

    char popFront() {
        if (isEmpty()) {
            return '\0';
        }
        char temp = data[front];
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }
        return temp;
    }

    char popBack() {
        if (isEmpty()) {
            return '\0';
        }
        char temp = data[rear];
        if (front == rear) {
            front = rear = -1;
        } else {
            rear--;
        }
        return temp;
    }

    int size() {
        if (isEmpty()) return 0;
        return rear - front + 1;
    }
};

int main() {
    Deque d;
    char palavra[100];
    cout << "Digite uma palavra: ";
    cin >> palavra;

    // Preenche o deque com os caracteres da palavra
    for (int i = 0; palavra[i] != '\0'; i++) {
        d.pushBack(palavra[i]);
    }

    bool palindromo = true;
    while (d.size() > 1) {
        char frente = d.popFront();
        char tras = d.popBack();
        if (frente != tras) {
            palindromo = false;
            break;
        }
    }

    if (palindromo) {
        cout << "É um palíndromo!" << endl;
    } else {
        cout << "Não é um palíndromo." << endl;
    }

    return 0;
}
