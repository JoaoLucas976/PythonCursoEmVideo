lista = []
lista.append(int(input("Insira um valor inteiro: ")))
continuar = input("Gostaria de continuar [S/N] ? ").strip().lower()
while continuar not in "sn":
    print("Escolha inválida")
    continuar = input("Gostaria de continuar [S/N] ? ").strip().lower()
while continuar != 'n':
    number = int(input("Insira um valor inteiro: "))
    if number not in lista:
        lista.append(number)
        print("Valor salvo com sucesso")
    else:
        print("Valor repetido, não irei adicionar")
    continuar = input("Gostaria de continuar [S/N] ? ").strip().lower()
    while continuar not in "sn":
        print("Escolha inválida")
        continuar = input("Gostaria de continuar [S/N] ? ").strip().lower()
lista.sort()
print(f"Você digitou os valores: {lista}")
