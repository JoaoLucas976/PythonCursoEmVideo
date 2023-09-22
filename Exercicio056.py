media_idades = 0
idade_homem_velho = 0
nome_homem_velho = "NOME"
mulher_nova = 0
for i in range(0, 4):
    print(f" | INDIVÍDUO NÚMERO {i + 1} | ")
    nome = input("Qual o seu nome ? ")
    sexo = input("Qual o seu sexo [M/F] ? ").lower().strip().replace(" ", "")
    idade = int(input("Qual a sua idade ? "))
    media_idades += idade
    if sexo == "m":
        if idade > idade_homem_velho:
            nome_homem_velho = nome
    else:
        if idade < 20:
            mulher_nova += 1

print(f"A media das idades é: {media_idades/4:.2f}")
print(f"O homem mais velho é: {nome_homem_velho}")
print(f"Existem {mulher_nova} mulheres com menos de 20 anos")
