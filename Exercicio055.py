peso = float(input("Insira o seu peso em KG: "))
menor = peso
maior = peso

for i in range(0,4):
    peso = float(input("Insira o seu peso em KG: "))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print(f"O maior peso foi: {maior}\nO menor peso foi: {menor}")