valor = int(input("Insira um valor inteiro: "))
lista = [valor]
cont = input("Deseja continuar ? [s/n] ").lower().strip()
while cont not in 'sn':
    print("Escolha inválida !")
    cont = input("Deseja continuar ? [s/n] ").lower().strip()
while cont != 'n':
    valor = int(input("Insira um valor inteiro: "))
    lista.append(valor)
    cont = input("Deseja continuar ? [s/n] ").lower().strip()
    while cont not in 'sn':
        print("Escolha inválida !")
        cont = input("Deseja continuar ? [s/n] ").lower().strip()
print(f"Foram digitados {len(lista)} valores")
lista.sort(reverse=True)
print(f"Foram digitados os valores (em ordem decrescente): {lista}")
if 5 in lista:
    print("O valor está na lista")
else:
    print("O valor não está na lista")
