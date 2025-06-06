from InterfoneResidencial import InterfoneResidencial
from InterfoneEmergencia import InterfoneEmergencia

def cadastrar():
    cadastros = []
    while True:
        while True:
            print('\n 1 - Interfone Residencial\n 2 - Servico de Emergencia')
            tipo = input('\n Tipo: ')
            if tipo == '1':
                interfone = InterfoneResidencial.cadastro()
                break
            elif tipo == '2':
                interfone = InterfoneEmergencia.cadastro()
                break
            else:
                print('\n ERRO: Opcao invalida !!!')
        cadastros.append(interfone)
        print('\n Deseja fazer um novo cadastro?\n 1 - Sim\n 2 - Nao')
        opcao = input('\n Opcao: ')
        if opcao == '1':
            continue
        elif opcao == '2':
            break
        else:
            print('\n ERRO: Opcao invalida !!!')
    return cadastros

def main():
    cadastros = cadastrar()

    for interfone in cadastros:
        print(interfone)
    print()

main()
