c = ('\033[m',         # 0 = sem cores
     '\033[0;30;41m',  # 1 = vermelho
     '\033[0;30;42m',  # 2 = verde
     '\033[0;30;43m',  # 3 = amarelo
     '\033[0;30;44m',  # 4 = azul
     '\033[0;30;45m',  # 5 = roxo
     '\033[0:30;47m'   # 6 = branco
     )


def escreva(txt, cor=0):
    n = len(txt) + 4
    print(c[cor], end='')
    print('-' * n)
    print('  ' + txt)
    print('-' * n)
    print(c[0], end='')


def ajuda(elem):
    from time import sleep
    escreva(f"Acessando o manual do comando {elem}", cor=4)
    sleep(1.5)
    print(c[5], end='')
    help(elem)
    print(c[0], end='')
    sleep(1.5)
    return elem


while True:
    escreva("SISTEMA DE AJUDA DE FUNÇÕES", cor=3)
    entrada = input("Função ou biblioteca: ")
    if entrada.strip().lower() == 'fim':
        escreva('FIM DO PROGRAMA', cor=1)
        break
    else:
        ajuda(entrada)
