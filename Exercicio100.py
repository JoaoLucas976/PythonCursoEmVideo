from random import randint


def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))
    print(lista)


def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos pares é: {soma}")


numeros = list()
sorteia(numeros)
somapar(numeros)
