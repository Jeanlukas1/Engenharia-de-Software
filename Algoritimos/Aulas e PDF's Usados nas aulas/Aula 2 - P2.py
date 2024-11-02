<<<<<<< HEAD
                                       #ARQUIVOS#

#biblioteca do sistema operacional
import os

#mudar o diretorio do arquivo
# os.chdir(r"c:\Users\UNIVASSOURAS\Documents\Evandro")

#usando excessoes caso o arquivo nao for encontrado ou outros erros
try:
    #criando arquivo de texto
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write("escrevendo alguma coisa! \n")  

    #abrindo e lendo o conteudo do arquivo
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

    #procurar onde o projeto foi salvo
    print(os.getcwd())

except FileExistsError:
    print("Arquivo não econtrado")

except PermissionError:
    print("Voce não tem permissão")

except Exception as e:
    print(f"Deu erro de {e}")

finally:
=======
                                       #ARQUIVOS#

#biblioteca do sistema operacional
import os

#mudar o diretorio do arquivo
# os.chdir(r"c:\Users\UNIVASSOURAS\Documents\Evandro")

#usando excessoes caso o arquivo nao for encontrado ou outros erros
try:
    #criando arquivo de texto
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write("escrevendo alguma coisa! \n")  

    #abrindo e lendo o conteudo do arquivo
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

    #procurar onde o projeto foi salvo
    print(os.getcwd())

except FileExistsError:
    print("Arquivo não econtrado")

except PermissionError:
    print("Voce não tem permissão")

except Exception as e:
    print(f"Deu erro de {e}")

finally:
>>>>>>> cc6279fd9b0c9ec82fb35247dd6445c0e80eca8b
    print("ate mais!")