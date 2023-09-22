dados = list()
nome = input("Insira o nome do aluno: ")
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
dados.append([nome, [nota1, nota2]])
escolha = input("Quer continuar ? [S/N] ").strip().lower()
while escolha not in "sn":
    print("Escolha inválida !")
    escolha = input("Quer continuar ? [S/N] ").strip().lower()

while escolha != "n":
    nome = input("Insira o nome do aluno: ")
    nota1 = float(input("Insira a nota 1: "))
    nota2 = float(input("Insira a nota 2: "))
    dados.append([nome, [nota1, nota2]])
    escolha = input("Quer continuar ? [S/N] ").strip().lower()
    while escolha not in "sn":
        print("Escolha inválida !")
        escolha = input("Quer continuar ? [S/N] ").strip().lower()

print("-" * 20)
print(f"{'DADOS ALUNOS':^20}")
print("-" * 20)
print(f"{'Nº':<4}",f"{'Nome':<6}",f"{'Media':>8}")
print("-" * 20)
for i in range(len(dados)):
    media = (dados[i][1][0] + dados[i][1][1])/2
    print(f"{i:<4}",f"{dados[i][0]:<6}",f"{media:>8}")

n = 0
while n != 999:
    n = int(input("De qual aluno você deseja ver as notas: (999 para finalizar)) "))
    while n > (len(dados) - 1) and n != 999:
        print("Escolha inválida !")
        n = int(input("De qual aluno você deseja ver as notas: (999 para finalizar)"))
    if n != 999:
        print(f"Notas de {dados[n][0]} são {dados[n][1][0]} e {dados[n][1][1]}")