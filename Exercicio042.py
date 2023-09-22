r1 = float(input("Insira o valor do seguimento de reta 1: "))
r2 = float(input("Insira o valor do seguimento de reta 2: "))
r3 = float(input("Insira o valor do seguimento de reta 3: "))

if (r1 > (r2 + r3)) or (r2 > (r1 + r3)) or (r3 > (r1 + r2)):
    print("Os 3 seguimentos não formam um triângulo")
else:
    if (r1 == r2) and (r2 == r3):
        print("Este é um triângulo equilátero")
    elif (r1 != r2) and (r2 != r3) and (r1 != r3):
        print("Este é um triângulo escaleno")
    else:
        print("Este é um triângulo isósceles")
