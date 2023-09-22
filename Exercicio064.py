n = int(input("Insira um número inteiro (999 para parar): "))
nt = 0
soma = 0
while n != 999:
    nt += 1
    soma += n
    n = int(input("Insira um número inteiro (999 para parar): "))
print(f"Você digitou {nt} valores e a soma deles é {soma}")
