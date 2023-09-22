def ficha(jog='desconhecido', gols=0):
    print(f"O jogador {jog} fez {gols} gols")


j = input("Insira o nome do jogador: ")
g = input("Insira o número de gols: ")
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == "":
    ficha(gols
          =g)
else:
    ficha(j, g)
