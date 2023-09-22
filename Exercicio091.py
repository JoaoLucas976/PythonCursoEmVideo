from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
for i in range(4):
    temp = "jogador" + str(i+1)
    jogadores[temp] = randint(1,6)
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.5)
ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ordenado):
    print(f"{i+1}º Lugar: {v[0]} tirou {v[1]} no dado")
    sleep(0.5)