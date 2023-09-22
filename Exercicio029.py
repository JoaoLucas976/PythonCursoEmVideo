velocidade = float(input("Insira a velocidade do carro: "))
if velocidade > 80:
    print("Você acaba de ser multado em R${:.2f}".format(7*(velocidade-80)))
else:
    print("Faça uma boa viagem")