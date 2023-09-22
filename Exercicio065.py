valor = int(input("Insira um valor inteiro: "))
maior = menor = soma = valor
n_valores = 1
escolha = input("Gostaria de continuar [S/N] ? ").upper()
while escolha != "N":
    if escolha != "S":
        print("Escolha inválida !!!")
        escolha = input("Gostaria de continuar [S/N] ? ").upper()
    else:
        valor = int(input("Insira um valor inteiro: "))
        soma += valor
        n_valores += 1
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        escolha = input("Gostaria de continuar [S/N] ? ").upper()
media = soma / n_valores
print(f"Você digitou {n_valores} valores")
print(f"A média deles é {media:.2f}")
print(f"O maior valor foi {maior}")
print(f"O menor valor foi {menor}")
