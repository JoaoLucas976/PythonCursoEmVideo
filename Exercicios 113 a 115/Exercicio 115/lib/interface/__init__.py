from toolbox import leiaInt, pintarTexto

def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{pintarTexto(str(c), cor=3)}{pintarTexto(" - " + str(item), cor=4)}')
        c += 1
    opc = leiaInt("Sua Opção: ")
    return opc
