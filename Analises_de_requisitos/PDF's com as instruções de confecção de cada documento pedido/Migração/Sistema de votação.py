opção_1 = []
opção_2 = []
opção_3 = []

def main(): 
    while True:
        
        print("Sistema de Votação")
        print("As opções são:")
        print("1. opção 1 \n 2. opção 2 \n 3. opção 3 \n 4. Sair") 
    
        entrada = int(input("Escolha uma opção: "))
        
        if entrada == 1:
           print("Votou na opção 1")
           opção_1.append(entrada)
        
        elif entrada == 2:
            print("Votou na opção 2") 
            opção_2.append(entrada)
    
        elif entrada == 3:
            print("Votou na opção 3")
            opção_3.append(entrada)
        
        elif entrada == 4:
            print("---- RESULTADOS DA VOTAÇÃO ----")
            print(f"Opção 1:", len(opção_1), "voto(s)")
            print(f"Opção 2:", len(opção_2), "voto(s)")
            print(f"Opção 3:", len(opção_3), "voto(s)")
            break
        else:
            print("Opção inválida! Digite novamente")
main()