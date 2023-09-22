num = s = 0
while True:
    n = int(input("Insira um número inteiro (999 para parar): "))
    if n == 999:
        break
    num += 1
    s += n
print(f"Você digitou {num} números e a soma deles é {s}")
