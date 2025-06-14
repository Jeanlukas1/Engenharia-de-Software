while True:
    try:
        qnt_ltrs = float(input("Digite a quantidade de litros abastecidos: "))
        prc_ltrs = float(input("Digite o preço pro litro: "))
        
        qnt_ltrs *= prc_ltrs
        
        print(f"Valor a pgar: {qnt_ltrs:.2f}")
        
    except ValueError:
        print(f"Digite um numero válido: {ValueError}")
    
    continuar = input("Deseja resgistrar outro abastecimento? (S/N)").upper()
    
    if continuar != "S":
        break
    