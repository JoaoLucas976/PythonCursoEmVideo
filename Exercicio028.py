from random import randint
from time import sleep
n_pc = randint(1, 5)
n_us = int(input("Adivinhe o número entre 1 e 5 pensado pelo computador: "))
print("PROCESSANDO...")
sleep(2)
if n_pc == n_us:
    print("Parabéns, você adivinhou")
else:
    print("infelizmente não foi dessa vez, eu pensei em {}".format(n_pc))
