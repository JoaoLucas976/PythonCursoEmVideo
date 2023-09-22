palavras = ("panqueca", "pudim", "sorvete", "bala", "chiclete", "pirulito")

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos as vogais: ", end="")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
            