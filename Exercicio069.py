print("Bem vindo ao analisador de idades")
pessoas18 = mulheres20 = homens = 0
while True:
    print("="*20)
    print("NOVO REGISTRO")
    print("=" * 20)
    idade = int(input("Digite o valor da idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa [M/F]: ").upper().strip()[0]
    while sexo not in "MF":
        print("Escolha inválida")
        sexo = input("Digite o sexo da pessoa [M/F]: ").upper().strip()[0]
    if idade > 18:
        pessoas18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1
    continuar = input("Gostaria de continuar [S/N] ? ").upper().strip()[0]
    while continuar not in "SN":
        print("Escolha inválida")
        continuar = input("Gostaria de continuar [S/N] ? ").upper().strip()[0]
    if continuar == "N":
        break
print(f"Ao todo foram cadastrados {pessoas18} pessoas com mais de 18 anos")
print(f"Ao todo foram cadastrados {homens} homens ")
print(f"Ao todo foram cadastrados {mulheres20} mulheres com menos de 20 anos")
