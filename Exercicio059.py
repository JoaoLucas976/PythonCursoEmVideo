from time import sleep

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

escolha = 0
while escolha != 5:
    escolha = int(input("Escolha a operação:"
                        "\n[1] Somar"
                        "\n[2] Multiplicar"
                        "\n[3] Maior"
                        "\n[4] Novos Valores"
                        "\n[5] Sair do Programa "
                        "\n"))
    if escolha == 1:
        resultado = n1 + n2
        print(f"A soma de {n1} e {n2} é {resultado}")
        sleep(1)
    elif escolha == 2:
        resultado = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é {resultado}")
        sleep(1)
    elif escolha == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n1 < n2:
            print(f"{n2} é maior que {n1}")
        sleep(1)
    elif escolha == 4:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
    elif escolha == 5:
        print("Obrigado por usar o nosso programa")
        sleep(2)
    else:
        print("Escolha uma opção válida")
        sleep(1)
