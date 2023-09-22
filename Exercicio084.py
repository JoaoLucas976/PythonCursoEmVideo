pessoas = list()
nome = input("Insira o nome: ")
peso = float(input("Insira o peso: "))
pessoas.append([nome, peso])
maiorpeso = peso
menorpeso = peso

escolha = input("Gostaria de continuar ? [S/N] ").strip().lower()
while escolha not in "sn":
    print("Escolha inválida")
    escolha = input("Gostaria de continuar ? [S/N] ").strip().lower()

while escolha != "n":
    nome = input("Insira o nome: ")
    peso = float(input("Insira o peso: "))
    pessoas.append([nome, peso])
    escolha = input("Gostaria de continuar ? [S/N] ").strip().lower()

    while escolha not in "sn":
        print("Escolha inválida")
        escolha = input("Gostaria de continuar ? [S/N] ").strip().lower()

for p in pessoas:
    if p[1] > maiorpeso:
        maiorpeso = p[1]
    if p[1] < menorpeso:
        menorpeso = p[1]

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso é {maiorpeso} e ele pertence a: ", end="")
for p in pessoas:
    if p[1] == maiorpeso:
        print(f"{p[0]} ", end="")
print()
print(f"O menor peso é {menorpeso} e ele pertence a: ", end="")
for p in pessoas:
    if p[1] == menorpeso:
        print(f"{p[0]} ", end="")
