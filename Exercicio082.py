valor = int(input("Digite um valor inteiro: "))
lista = [valor]
escolha = input("Você deseja continuar ? [s/n] ")
while escolha not in 'sn':
    print("Escolha inválida !")
    escolha = input("Você deseja continuar ? [s/n] ")
while escolha != 'n':
    valor = int(input("Digite um valor inteiro: "))
    lista.append(valor)
    escolha = input("Você deseja continuar ? [s/n] ")
    while escolha not in 'sn':
        print("Escolha inválida !")
        escolha = input("Deseja continuar ? [s/n] ").lower().strip()

pares = []
impares = []
for var in lista:
    if var % 2 == 0:
        pares.append(var)
    else:
        impares.append(var)

print(f"Foram digitados os valores: {lista}")
print(f"Os valores pares foram: {pares}")
print(f"Os valores impares foram: {impares}")