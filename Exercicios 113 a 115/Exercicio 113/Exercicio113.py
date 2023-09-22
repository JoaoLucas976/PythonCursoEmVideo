from toolbox import pintarTexto


def leiaInt(txt):
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
            print(pintarTexto("TUDO CERTO! TENHA UM BOM DIA", cor=2))
            return n


def leiaFloat(txt):
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
            print(pintarTexto("TUDO CERTO! TENHA UM BOM DIA", cor=2))
            return n


num = leiaInt("Digite um número inteiro: ")
num2 = leiaFloat("Digite um número real: ")
