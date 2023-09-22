a0 = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão da PA: "))
n = int(input("Quantos termos da PA você gostaria de ver ? "))
i = n
t = 0
while n != 0:
    if i == 0:
        n = int(input("Quantos termos mais da PA você gostaria de ver ? "))
        i = n
    else:
        print(f"O termo {t+1} da PA é: {a0 + r*t}")
        t += 1
        i -= 1
