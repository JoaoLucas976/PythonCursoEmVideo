soma = 0
for i in range(1, 7):
    num = int(input("Insira um número inteiro: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares é: {soma}")
