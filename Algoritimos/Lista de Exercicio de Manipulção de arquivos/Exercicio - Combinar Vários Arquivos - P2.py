#  - Crie um programa que leia o conteúdo de três arquivos (`parte1.txt`, `parte2.txt` e 
# `parte3.txt`). 
#    - Combine o conteúdo dos três arquivos em um novo arquivo chamado `texto_completo.txt`

with open("parte1.txt", "w") as arquivo1:
    arquivo1.write("Ola Mundo!")

with open("parte2.txt", "w") as arquivo2:
    arquivo2.write("Sou muito")
    
with open("parte3.txt", "w") as arquivo3:
    arquivo3.write("Bom!")    

with open("texto_completo", "w") as arquivo4:
    arquivo4.write("")
    
