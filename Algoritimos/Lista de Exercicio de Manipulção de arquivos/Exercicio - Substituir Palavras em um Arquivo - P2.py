
# Substituir Palavras em um Arquivo
#  - Crie um programa que leia o conteúdo de um arquivo `texto.txt`.
#  - Substitua todas as ocorrências de uma palavra (por exemplo, "Python") por outra (por
#  exemplo, "programação") e salve o conteúdo alterado em um novo arquivo chamado
# `texto_modificado.txt`.

with open('texto.txt', 'r') as arquivo1:
    conteudo = arquivo1.read()
    
novo_conteudo = conteudo.replace('mundo', 'Programação')

with open('texto_modificado.txt', 'w') as arquivo2:
    arquivo2.write(novo_conteudo)
    
        
    