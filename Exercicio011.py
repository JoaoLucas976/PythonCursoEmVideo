altura = float(input("Insira o valor da altura da parede: "))
largura = float(input("Insira o valor da largura da parede: "))
area = altura*largura
print("O valor da área da parede é: {}, são necessários {} litros de tinta para pinta-la".format(area,(area/2)))