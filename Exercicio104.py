def leiaInt(n):
    while not n.isnumeric():
        print(f"Entrada inválida !")
        n = input('Digite um número inteiro: ')
    return n


n = leiaInt(input('Digite um número inteiro: '))
print(f"Você acabou de digitar o número {n}")
