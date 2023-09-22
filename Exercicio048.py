soma = 0
cont = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        soma += i
        cont += 1
print(f"A soma de todos os {cont} múltiplos ímpares de 3 entre 1 e 500 é {soma}")
