matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        matriz[i].append(float(input(f"Insira o elemento matriz[{i}][{j}]: ")))
for i in range(3):
    print("|", end="")
    for j in range(3):
        print(f" {matriz[i][j]:^5} |", end="")
    print()