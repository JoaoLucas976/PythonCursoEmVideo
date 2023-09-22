from random import randint
from time import sleep

sleep(0.5)
print("BEM VINDO AO ADIVINHA AÍ 2.0")
dif = int(input("Escolha o nível de dificuldade:\n"
                "[1] Fácil\n"
                "[2] Médio\n"
                "[3] Difícil\n"
                "[4] Hardcore\n"))
while dif not in [1, 2, 3, 4]:
    print("Escolha inválida")
    dif = int(input("Escolha o nível de dificuldade:\n"
                    "[1] Fácil\n"
                    "[2] Médio\n"
                    "[3] Difícil\n"
                    "[4] Hardcore\n"))

if dif == 1:
    maxim = 10
elif dif == 2:
    maxim = 100
elif dif == 3:
    maxim = 1000
elif dif == 4:
    maxim = 10000

n_pc = randint(1, maxim)
n_us = int(input(f'Adivinhe o número entre 1 e {maxim} pensado pelo computador: '))
palpites = 1
print("PROCESSANDO...")
sleep(0.5)
while n_us != n_pc:
    if n_us > n_pc:
        print("MENOS. Tente novamente")
    elif n_pc > n_us:
        print("MAIS. Tente novamente")
    n_us = int(input(f"Adivinhe o número entre 1 e {maxim} pensado pelo computador: "))
    palpites += 1
    print("PROCESSANDO...")
    sleep(0.5)
print("Parabéns, você adivinhou o número que eu pensei !")
print(f"Você adivinhou em {palpites} palpites")
