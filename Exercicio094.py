pessoas = list()
pessoa = dict()
mulheres = list()
acima_media = list()
totidade = 0
pessoa['nome'] = input("Insira o nome: ").strip()
pessoa['sexo'] = input("Insira o sexo da pessoa: [M/F] ").strip().upper()
pessoa['idade'] = int(input("Insira a idade da pessoa: "))
totidade += pessoa['idade']
pessoas.append(pessoa.copy())
escolha = input("Quer continuar ? [S/N] ").strip().lower()
while escolha not in "sn":
    print("Escolha inválida !")
    escolha = input("Quer continuar ? [S/N] ").strip().lower()
while escolha != 'n':
    pessoa['nome'] = input("Insira o nome: ").strip()
    pessoa['sexo'] = input("Insira o sexo da pessoa: [M/F] ").strip().upper()
    pessoa['idade'] = int(input("Insira a idade da pessoa: "))
    totidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    escolha = input("Quer continuar ? [S/N] ").strip().lower()
    while escolha not in "sn":
        print("Escolha inválida !")
        escolha = input("Quer continuar ? [S/N] ").strip().lower()
media = totidade/len(pessoas)
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'][:])
    if pessoa['idade'] > media:
        acima_media.append(pessoa['nome'][:])
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"A média de idade é {media}")
print(f"As mulheres são: {mulheres}")
print(f"As pessoas com idade acima da média são: {acima_media}")
