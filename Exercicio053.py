frase = input("Insira uma frase sem pontuações: ")
frase1 = frase.strip().replace(" ","").lower()
frase2 = ""
# frase2 = frase1[::-1]
for i in range(len(frase1) - 1, -1, -1):
    frase2 += frase1[i]
if frase1 == frase2:
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")
