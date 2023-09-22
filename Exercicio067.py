while True:
    n = int(input("Insira um número inteiro para mostrar sua tabuada (negativo para parar): "))
    if n < 0:
        break
    for i in range(1,11):
        print(f" {n} x {i} = {n*i}")
print("Fim do Programa")
