n = int(input("Insira o número de termos da Sequência de Fibonacci: "))
i = 0
t1 = 1
t2 = 1
while i < n:
    if i < 2:
        print(f"O {i + 1}º termo da sequencia é 1")
    else:
        print(f"O {i + 1}º termo da sequencia é {t1 + t2}")
        t1, t2 = t2, t1 + t2
    i += 1
