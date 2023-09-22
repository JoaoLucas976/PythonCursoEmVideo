numero1 = float(input("Insira um número: "))
maior = numero1
menor = numero1
numero2 = float(input("Insira outro número: "))
if numero2 > maior:
    maior = numero2
if numero2 < menor:
    menor = numero2
numero3 = float(input("Insira mais um número: "))
if numero3 > maior:
    maior = numero3
if numero3 < menor:
    menor = numero3
print("O maior numero foi {}\nO menor número foi {}".format(maior, menor))
