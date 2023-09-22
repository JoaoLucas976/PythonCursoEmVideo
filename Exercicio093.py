jogador = dict()
gols = list()
tot = 0
jogador['Nome'] = input("Nome: ")
jogador['Numero de partidas'] = int(input("Número de partidas: "))
for i in range(jogador['Numero de partidas']):
    gols += [int(input(f"Quantos gols o jogador fez no jogo {i+1}: "))]
jogador['gols'] = gols
for gol in gols:
    tot += gol
jogador['total de gols'] = tot

for k, v in jogador.items():
    print(f"{k} tem valor {v}")

print(f"O jogador {jogador['Nome']} jogou {jogador['Numero de partidas']} partidas")
temp = len(jogador['gols'])
for i in range(temp):
    print(f"    => Na partida {i} fez {jogador['gols'][i]}")
print(f"Um total de {jogador['total de gols']} gols")