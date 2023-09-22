valores = [[],[]]

for i in range(7):
    num = int(input(f"Insira o {i+1}º valor inteiro: "))

    if num % 2 == 1:
        valores[1].append(num)
    else:
        valores[0].append(num)

valores[0].sort()
valores[1].sort()
print(f"Valores pares: {valores[0]}")
print(f"Valores impares: {valores[1]}")