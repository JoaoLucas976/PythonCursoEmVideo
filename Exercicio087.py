matriz = [[],[],[]]
somap = soma3 = maior2 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(float(input(f"Insira o elemento matriz[{i}][{j}]: ")))

for i in range(3):
    print("|", end="")
    for j in range(3):
        print(f" {matriz[i][j]:^5} |", end="")
        if i == 1:
            maior2 = matriz[i][j]
    print()

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            somap += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior2:
                maior2 = matriz[i][j]

print(f"A soma dos pares é: {somap}")
print(f"A soma dos valores da terceira coluna é: {soma3}")
print(f"O maior valor da segunda linha é {maior2}")
