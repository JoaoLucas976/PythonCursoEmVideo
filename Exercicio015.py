dias = int(input("Insira o numero de dias que o carro foi alugado: "))
km = float(input("Insira o numero de km rodados no carro: "))
preco = 60 * dias + 0.15 * km
print("O preco total a pagar é R${:.2f}".format(preco))