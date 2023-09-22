def notas(*kwargs, situacao=False):
    """
    :param kwargs: valor das notas do aluno
    :param situacao: opcional, retorna a situação do aluno
    :return: sem retorno
    """
    dados = dict()
    n = len(kwargs)
    soma = 0
    for nota in kwargs:
        soma += nota
    dados['total'] = n
    dados['menor'] = min(kwargs)
    dados['maior'] = max(kwargs)
    dados['media'] = round(soma/n, 2)
    if situacao:
        if dados['media'] < 5:
            dados['situacao'] = "RUIM"
        elif 5 <= dados['media'] < 7:
            dados['situacao'] = "RAZOAVEL"
        elif 7 <= dados['media'] < 9:
            dados['situacao'] = "BOA"
        else:
            dados['situacao'] = "EXCELENTE"
    print(dados)
    return 0


resp = notas(5.5, 6.5, 8, 10, 10, situacao=True)
help(notas)
