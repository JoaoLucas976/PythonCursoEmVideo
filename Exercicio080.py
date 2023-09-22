lista = []
for i in range(0,5):
    a = int(input("Digite um valor inteiro: "))
    if i == 0 or a > lista[-1]:
        lista.append(a)
        print("Adicionado ao final da lista!")
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos, a)
                print(f"Adicionado na posição {pos} da lista! ")
                break
            pos += 1

print(f"Os valores digitados foram: {lista}")
