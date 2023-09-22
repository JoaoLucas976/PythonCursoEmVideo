from math import trunc

numero = float(input("Insira um numero quebrado: "))
inteira = trunc(numero)
print("A parte inteira de {} é {}".format(numero, inteira))
print("A parte inteira de {} é {}".format(numero, int(inteira)))