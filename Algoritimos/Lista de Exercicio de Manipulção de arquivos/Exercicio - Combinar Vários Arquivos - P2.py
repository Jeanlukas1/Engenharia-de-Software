#  - Crie um programa que leia o conteúdo de três arquivos (`parte1.txt`, `parte2.txt` e 
# `parte3.txt`). 
#    - Combine o conteúdo dos três arquivos em um novo arquivo chamado `texto_completo.txt`

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: o arquivo {nome_arquivo} não foi encontrado.")
        return ''

def combinar_arquivos():
    parte1 = ler_arquivo('parte1.txt')
    parte2 = ler_arquivo('parte2.txt')
    parte3 = ler_arquivo('parte3.txt')

    conteudo_completo = parte1 + '\n' + parte2 + '\n' + parte3

    with open('texto_completo.txt', 'w', encoding='utf-8') as arquivo_completo:
        arquivo_completo.write(conteudo_completo)

    print("O conteúdo dos arquivos foi combinado em 'texto_completo.txt'.")

combinar_arquivos()

