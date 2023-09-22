from random import randint
print("Vamos jogar Par ou Impar ?")
vitorias = 0

while True:
    jogador = int(input("Insira um número (0 a 10): "))
    while jogador not in [0,1,2,3,4,5,6,7,8,9,10]:
        print("Escolha inválida")
        jogador = int(input("Insira um número (0 a 10): "))
    maquina = randint(0, 10)
    escolha = input("Você escolha par ou impar [P/I] ? ").upper().strip()[0]
    while escolha not in "PI":
        print("Escolha inválida")
        escolha = input("Você escolha par ou impar [P/I] ? ").upper().strip()[0]
    resultado = jogador + maquina
    print(f"O computador jogou {maquina}, você jogou {jogador}")
    print(f"O resultado foi: {resultado}")
    if escolha == "P":
        if resultado % 2 == 0:
            print("Você ganhou, vamos jogar novamente !")
            vitorias += 1
        else:
            print("Você perdeu, mais sorte na próxima")
            break
    else:
        if resultado % 2 == 1:
            print("Você ganhou, vamos jogar novamente !")
            vitorias += 1
        else:
            print("Você perdeu, mais sorte na próxima")
            break

print(f"Você ganhou {vitorias} vezes seguidas. ")