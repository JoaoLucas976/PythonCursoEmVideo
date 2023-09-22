def aumentar(n=0, p=0, form=False):
    """
    :param n: Valor a ser aumentado
    :param p: Taxa percentual do aumento
    :param form: Escolhe se o valor será formatado em formato de moeda
    :return: Retorna o valor aumentado
    """
    res = n * (1 + (p/100))
    if form:
        return moeda(res)
    return res


def dobro(n=0, form=False):
    """
    :param n: Valor a ser dobrado
    :param form: Escolhe se o valor será formatado em formato de moeda
    :return: Retorna o dobro do valor
    """
    res = 2 * n
    if form:
        return moeda(res)
    return res


def metade(n=0, form=False):
    """
    :param n: Valor a ser dividido
    :param form: Escolhe se o valor será formatado em formato de moeda
    :return: Retorna a metade do valor
    """
    res = n / 2
    if form:
        return moeda(res)
    return res


def diminuir(n=0, p=0, form=False):
    """
    :param n: Valor a ser calculado
    :param p: Taxa percentual da diminuição
    :param form: Escolhe se o valor será formatado em formato de moeda
    :return: Retorna o valor diminuído
    """
    res = n * (1 - (p/100))
    if form:
        return moeda(res)
    return res


def moeda(n=0):
    """
    :param n: Valor a ser formatado
    :return: Retorna o valor formatado em formato de moeda
    """
    res = f"R${n:.2f}"
    return res.replace('.', ',')


def resumo(n=0, a=0, d=0):
    """
    :param n: Valor base dos cálculos
    :param a: Percentual do aumento
    :param d: Percentual da diminuição
    :return: Retorna um resumo dos valores calculados
    """
    print(f"O dobro de {moeda(n)} é {dobro(n, True)}")
    print(f"A metade de {moeda(n)} é {metade(n, True)}")
    print(f"Aumentando {a}% de {moeda(n)} temos {aumentar(n, a, True)}")
    print(f"Diminuindo {d}% de {moeda(n)} temos {diminuir(n, d, True)}")
