def leiaDinheiro(msg):
    valido = False
    while not valido:
        ent = str(input(msg)).replace(',', '.')
        if ent.isalpha():
            print(f"ERRO {ent} não é um preço válido !")
        else:
            return float(ent)


def leiaInt(n):
    while not n.isnumeric():
        print(f"Entrada inválida !")
        n = input('Digite um número inteiro: ')
    return n
