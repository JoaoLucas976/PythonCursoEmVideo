def fatorial(n, show=False):
    """
    --> Função para calculo de fatorial
    :param n: número do qual será calculado o fatorial
    :param show: opcional, mostra o passo-a-passo do cálculo
    :return: retorna o valor do fatorial
    """
    c = n
    fat = 1
    while c >= 1:
        fat *= c
        c -= 1
    if show:
        txt = ""
        c = n
        while c > 1:
            txt += f"{c} x "
            c -= 1
        txt += "1"
        return f"Fatorial de {n}: " + txt + f" = {fat}"
    return f"Fatorial de {n}: {fat}"


print(fatorial(5, show=True))
help(fatorial)
