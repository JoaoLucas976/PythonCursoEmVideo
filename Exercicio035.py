r1 = float(input("Insira o valor do comprimento de reta 1: "))
r2 = float(input("Insira o valor do comprimento de reta 2: "))
r3 = float(input("Insira o valor do comprimento de reta 3: "))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[0;32m',
         'vermelho': '\033[0;31m'}
if r1 > (r2 + r3) or r2 > (r1 + r3) or r3 > (r1 + r2):
    print("As 3 retas {}não formam{} um triângulo".format(cores['vermelho'], cores['limpa']))
else:
    print("As 3 retas {}formam{} um triângulo".format(cores['verde'], cores['limpa']))

# \033[0;31;44m # Texto vermelho
# \033[0;32;44m # Texto verde
