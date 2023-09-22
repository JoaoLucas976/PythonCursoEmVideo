def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if (fim < inicio) and passo > 0:
        passo = - passo
    if (fim > inicio) and passo < 0:
        passo = - passo
    if (fim > inicio) and passo > 0:
        fim += 1
    if fim < inicio:
        fim -= 1
    for c in range(inicio, fim, passo):
        print(c)


contador(1,10,-1)
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
