print("="*30)
print(f"{'Banco do Brasil':^30}")
print("="*30)
cel50 = cel20 = cel10 = cel1 = 0
while True:
    valor = int(input("Escolha o valor que deseja sacar: R$"))
    saque = valor
    while True:
        if saque // 50 >= 1:
            cel50 += 1
            saque -= 50
        elif saque // 20 >= 1:
            cel20 += 1
            saque -= 20
        elif saque // 10 >= 1:
            cel10 += 1
            saque -= 10
        else:
            cel1 = saque
            break

    print(f"Para fazer o saque de {valor:.2f} são necessárias")
    if cel50 > 0:
        print(f"{cel50} células de R$ 50.00")
    if cel20 > 0:
        print(f"{cel20} células de R$ 20.00")
    if cel10 > 0:
        print(f"{cel10} células de R$ 10.00")
    if cel1 > 0:
        print(f"{cel1} células de R$ 1.00")

    escolha = input("Fazer nova operação [S/N] ? ").strip().upper()[0]
    while escolha not in "SN":
        print("Escolha inválida")
        escolha = input("Fazer nova operação [S/N] ? ").strip().upper()[0]
    if escolha == "N":
        break
print("Obrigado por usar nosso caixa. Volte Sempre")
