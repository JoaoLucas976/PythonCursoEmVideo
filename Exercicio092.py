from datetime import date
ano_atual = date.today().year
cadastro = dict()
cadastro['Nome'] = input("Nome: ")
cadastro['Idade'] = ano_atual - int(input("Ano de Nascimento: "))
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] == 0:
      for k, v in cadastro.items():
            print(f"    - {k} tem o valor {v}")
else:
      cadastro['Ano de Contratação'] = int(input("Ano de contratação: "))
      cadastro['Salário'] = float(input("Salário: "))
      for k, v in cadastro.items():
            print(f"    - {k} tem o valor {v}")
      aposent = cadastro['Idade'] + 35 - (ano_atual - cadastro['Ano de Contratação'])
      print(f"Você irá se aposentar com {aposent} anos")
