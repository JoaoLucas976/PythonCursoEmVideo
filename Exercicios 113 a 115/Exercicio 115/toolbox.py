def pintarTexto(txt="", cor=0):
    """
    Função para printar textos coloridos
    :param txt: Texto a ser pintado
    :param cor: Número da cor desejada
    cor = 1: vermelho; cor = 2: verde;
    cor = 3: amarelo;  cor = 4: azul;
    cor = 5: roxo;     cor = 6: branco;
    :return: Retorna o texto colorido
    """
    c = ('\033[m',         # 0 = sem cores
         '\033[0;31m',  # 1 = vermelho
         '\033[0;32m',  # 2 = verde
         '\033[0;33m',  # 3 = amarelo
         '\033[0;34m',  # 4 = azul
         '\033[0;35m',  # 5 = roxo
         '\033[0:36m'   # 6 = branco
         )
    ntxt = c[cor] + txt + c[0]
    return ntxt


def leiaInt(txt):
    """
    Função para ler números inteiros com tratamento de erro
    :param txt: Texto apresentado na caixa de input
    :return: Retorna o valor lido caso ele seja inteiro
    """
    while True:
        try:
            n = int(input(txt))
        except KeyboardInterrupt:
            print(pintarTexto("\nUsuário desistiu!", cor=3))
            return 0
        except (TypeError, ValueError):
            print(pintarTexto("Número inválido", cor=1))
            continue
        else:
            return n


def leiaFloat(txt):
    """
    Função para ler números reais com tratamento de erro
    :param txt: Texto apresentado na caixa de input
    :return: Retorna o valor lido caso ele seja real
    """
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print(pintarTexto("Número inválido! ", cor=1))
            continue
        except KeyboardInterrupt:
            print("Operação cancelada pelo usuário")
            return 0
        else:
            return n
