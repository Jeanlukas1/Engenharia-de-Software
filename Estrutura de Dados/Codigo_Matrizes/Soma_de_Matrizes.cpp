#include <stdlib.h>
#include <iostream>

using namespace std;

int main() {
    int n, m;

    cout << "Digite o número de linhas e colunas: ";
    cin >> n >> m;
    cin >> n >> m;

    int a[n][m], b[n][m], c[n][m];

    cout << "Digite os elementos da matriz A:" << endl;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> a[i][j];

    cout << "Digite os elementos da matriz B:" << endl;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> b[i][j];

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            c[i][j] = a[i][j] + b[i][j];

    cout << "Matriz resultante (A + B):" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            cout << c[i][j] << " ";
        cout << endl;
    }

    return 0;
}
