distancia = float(input("Insira a distância da viagem em KM: "))
if distancia <= 200:
    custo = 0.5 * distancia
else:
    custo = 0.45 * distancia
print("O custo da sua viagem será R${:.2f}".format(custo))