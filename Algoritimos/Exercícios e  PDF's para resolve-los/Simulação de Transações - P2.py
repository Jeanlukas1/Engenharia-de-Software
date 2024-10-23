# 5. Simulação de transações: Crie um programa que simule uma transferência 
# bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o 
# saldo seja insuficiente, levante uma exceção do tipo ValueError com a 
# mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o 
# usuário. 

def realizar_transferencia():
    try:

        saldo = float(input("Informe o saldo da conta: R$ "))
        
        valor_transferencia = float(input("Informe o valor da transferência: R$ "))
        
        if valor_transferencia > saldo:
            raise ValueError("Saldo insuficiente")
        
        saldo -= valor_transferencia
        print(f"Transferência de R$ {valor_transferencia} realizada com sucesso!")
        print(f"Novo saldo: R$ {saldo:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    realizar_transferencia()
