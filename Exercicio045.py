from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input("Escolha uma jogada:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n"))
computador = randint(1,3)
# 1 = pedra, 2 = papel, 3 = tesoura
if (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
    print(f"Você jogou {itens[jogador - 1]} e o computador jogou {itens[computador - 1]}")
    print("Você \033[32mganhou\033[m do computador")
elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 3) or (jogador == 3 and computador == 1):
    print(f"Você jogou {itens[jogador - 1]} e o computador jogou {itens[computador - 1]}")
    print("Você \033[31mperdeu\033[m para o computador")
elif jogador not in (1, 2, 3):
    print('Opção inválida')
else:
    print(f"Você jogou {itens[jogador - 1]} e o computador jogou {itens[computador - 1]}")
    print("Você \033[34mempatou\033[m com o computador")
