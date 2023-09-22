a0 = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão da PA: "))
for i in range(0, 11):
    print(f"O termo {i} da PA é: {a0 + r*i}")
