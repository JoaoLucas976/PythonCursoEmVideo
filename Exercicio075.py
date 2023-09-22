tupla = (int(input("Insira um numero inteiro: ")),
         int(input("Insira mais um numero inteiro: ")),
         int(input("Insira outro numero inteiro: ")),
         int(input("Insira o último numero inteiro: ")))

print(f"O número 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O número 3 apareceu primeiro na posição {tupla.index(3) + 1}")
else:
    print("O número 3 não aparece nos valores digitados")

print("Os números pares digitados foram: ", end=" ")
for n in tupla:
    if n % 2 == 0 and n != 0:
        print(n, end=" ")