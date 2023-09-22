def acharmaior(* numeros):
    cont = maior = 0
    for num in numeros:
        if cont == 0:
            maior = num
        if num > maior:
            maior = num
        cont += 1
    print(f"O maior é {maior}")


acharmaior(1, 2, 3, 4, 8, 6, 35, 23, 3)
