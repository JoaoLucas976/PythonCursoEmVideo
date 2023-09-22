expressao = input("Insira uma expressão: ")
lista = list(expressao)
abre = 0
fecha = 0
for letra in lista:
    if letra == '(':
        abre += 1
    if letra == ")":
        fecha += 1
if abre == fecha:
    print("Essa expressão é válida")
else:
    print("Essa expressão é inválida")
