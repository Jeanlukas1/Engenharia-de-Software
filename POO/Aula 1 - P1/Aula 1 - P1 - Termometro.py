termometer = float(input("Digite o grau em que se encontra o Paciente: ")) 

if termometer >= 32.0 and termometer <= 35.0:
    print("Condição:             Descrição:")
    print("Hiportemia Leve       Pode haver tremores, calafrios e dificuldade de coordenação.\n                      A pessoa ainda consegue se mover, mas sente desconforto.")
elif termometer >= 28.0 and termometer <= 32.0:
    print("Condição:                Descrição:")
    print("Hiportemia Moderada      Tremores fortes, fala arrastada, confusão mental, respiração mais lenta,\n                      perda de coordenação motora.")
elif termometer < 28.0:
    print("Condição:              Descrição:")
    print("Hipotermia Grave       A pessoa pode perder a consciência, a respiração se torna muito lenta ou irregular, \n                       e o risco de falência dos órgãos aumenta.")

elif termometer > 37.0 and termometer <= 38.0:
    print("Condição:       Descrição:")
    print("Pré-febre       A temperatura começa a subir, mas ainda não atingiu o nível de febre.\n                Pode haver sensação de cansaço ou desconforto.")
elif termometer >= 38.0 and termometer <= 39.9:
    print("Condição:      Descrição:")
    print("Febre          O corpo reage a infecções ou inflamações. Pode haver calafrios, dor no corpo,\n               suor excessivo e sensação de calor.")
elif termometer >= 40.0:
    print("Condição:      Descrição:")
    print("Febre Alta     Temperatura muito alta, com risco de complicações graves como\n               desidratação, confusão mental e falência de órgãos.")

elif termometer >= 36.1 and termometer <= 37.0:
    print("Condição:      Descrição:")
    print("Normal         Faixa normal de temperatura do corpo, sem sinais de febre ou hipotermia.")