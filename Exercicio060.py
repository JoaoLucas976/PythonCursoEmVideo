n = int(input("Insira um número e calcule o seu fatorial: "))
i = n - 1
fatorial = n
while i != 0:
    fatorial *= i
    i -= 1
print(f"O fatorial de {n} é {fatorial}")