numero = int(input("Insira um número: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando o numero {}".format(numero))
print("Unidade: {}".format(u))
print("Dezena:  {}".format(d))
print("Centeza: {}".format(c))
print("Milhar:  {}".format(m))
