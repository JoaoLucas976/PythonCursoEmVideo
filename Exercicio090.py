dados = dict()
dados['nome'] = input("Insira o nome do aluno: ")
dados['media'] = float(input("Insira a média do aluno: "))
if dados['media'] >= 5:
    dados['situacao'] = 'aprovado'
else:
    dados['situacao'] = 'reprovado'
for k, v in dados.items():
    print(f"{k} é igual a {v}")
