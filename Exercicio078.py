lista = []
imaior = []
imenor = []
for i in range(5):
    lista.append(int(input("Insira um valor inteiro: ")))
for i, v in enumerate(lista):
    if v == max(lista):
        imaior.append(i)
    if v == min(lista):
        imenor.append(i)
print(f"O maior valor foi {max(lista)} e ele se encontra nas posições: ", end="")
for i in imaior:
    print(f"{i}...", end="")
print(" ")
print(f"O menor valor foi {min(lista)} e ele se encontra nas posições: ", end="")
for i in imenor:
    print(f"{i}...", end=" ")
