jogador = dict()
jogadores = list()
gols = list()
cod = 0
tot = 0
jogador['cod'] = cod
cod += 1
jogador['nome'] = input("Nome: ")
jogador['njogos'] = int(input("Jogou em quantas partidas ? "))
for i in range(jogador['njogos']):
    gol = int(input(f"Quantos gols no jogo {i + 1} ? "))
    gols += [gol]
    tot += gol
jogador['gols'] = gols
jogador['total'] = tot
jogadores.append(jogador.copy())
escolha = input("Quer continuar ? [S/N] ").strip().lower()
while escolha not in 'sn':
    print("Escolha inválida !")
    escolha = input("Quer continuar ? [S/N]").strip().lower()
while escolha != 'n':
    gols = []
    tot = 0
    jogador['cod'] = cod
    cod += 1
    jogador['nome'] = input("Nome: ")
    jogador['njogos'] = int(input("Jogou em quantas partidas ? "))
    for i in range(jogador['njogos']):
        gol = int(input(f"Quantos gols no jogo {i + 1} ? "))
        tot += gol
        gols += [gol]
    jogador['gols'] = gols
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    escolha = input("Quer continuar ? [S/N] ").strip().lower()
    while escolha not in 'sn':
        print("Escolha inválida !")
        escolha = input("Quer continuar ? [S/N]").strip().lower()

print(f"-=" * 20)
print(f"{'cod':<5}", f"{'Nome':<20}", f"{'gols':<10}", f"{'total':>5}")
print(f"-=" * 20)
for jg in jogadores:
    print(f"{jg['cod']:<5} {jg['nome']:<20} {str(jg['gols']):<10} {jg['total']:^5}")
print(f"-=" * 20)
esc = int(input("Qual jogador você quer ver o relatório ? (999 parar) "))
while esc != 999 and esc < len(jogadores):
    print(f"Levantamento do jogador {jogadores[esc]['nome']}")
    for i, g in enumerate(jogadores[esc]['gols']):
        print(f"No jogo {i+1} fez {g} gols")
    esc = int(input("Qual jogador você quer ver o relatório ? (999 parar) "))
print(f"Fim do programa")