MAX_VAGAS = 100

def inicializar_estacionamento():
    return [{'id': i + 1, 'placa': '', 'ocupado': False} for i in range(MAX_VAGAS)]

def exibir_vagas(estacionamento):
    print("Vagas disponíveis:")
    for vaga in estacionamento:
        if not vaga['ocupado']:
            print(f"Vaga {vaga['id']} está livre.")

def estacionar_veiculo(estacionamento):
    placa = input("Informe a placa do veículo: ")
    for vaga in estacionamento:
        if not vaga['ocupado']:
            vaga['ocupado'] = True
            vaga['placa'] = placa
            print(f"Veículo com placa {placa} estacionado na vaga {vaga['id']}.")
            return
    print("Estacionamento cheio!")

def remover_veiculo(estacionamento):
    placa = input("Informe a placa do veículo a ser removido: ")
    for vaga in estacionamento:
        if vaga['ocupado'] and vaga['placa'] == placa:
            vaga['ocupado'] = False
            print(f"Veículo com placa {placa} removido da vaga {vaga['id']}.")
            return
    print("Veículo não encontrado.")

def main():
    estacionamento = inicializar_estacionamento()
    opcao = 0

    while opcao != 4:
        print("\nSistema de Gerenciamento de Estacionamento")
        print("1. Exibir Vagas")
        print("2. Estacionar Veículo")
        print("3. Remover Veículo")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            exibir_vagas(estacionamento)
        elif opcao == 2:
            estacionar_veiculo(estacionamento)
        elif opcao == 3:
            remover_veiculo(estacionamento)
        elif opcao == 4:
            print("Saindo do sistema...")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
