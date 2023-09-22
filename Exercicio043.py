peso = float(input("Insira o seu peso em Kg: "))
altura = float(input("Insira a sua altura em metros: "))
IMC = peso / altura ** 2
print("O IMC ideal é entre 18.5 e 25")
print(f'Seu IMC é {IMC:.2f}')
if IMC < 18.5:
    print("\033[33mAbaixo do peso\033[m")
elif IMC >= 18.5 and IMC < 25:
    print("\033[32mPeso ideal\033[m")
elif IMC >= 25 and IMC < 30:
    print("\033[33mSobrepeso\033[m")
elif IMC >= 30 and IMC < 40:
    print("\033[31mObesidade\033[m")
else:
    print("\033[4;31;40mObesidade Mórbida\033[m")
