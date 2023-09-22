sexo = input("Insira o seu sexo [M/F]: ").strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print("Escolha inválida !!!")
    sexo = input("Insira o seu sexo [M/F]: ").strip().upper()[0]
print(f"Você escolheu: {sexo}")
