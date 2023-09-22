from random import randint
from time import sleep
jogo = list()
jogos = list()
n = int(input("Insira o número de jogos a ser definidos: "))
sleep(0.5)
print("-=-="*5)
print(f" DEFININDO {n} JOGOS ")
print("-=-="*5)
sleep(0.5)
for i in range(n):
    for j in range(6):
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for i in range(n):
    print(f"Jogo {i+1}: {jogos[i]}")
    sleep(1)
