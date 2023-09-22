for i in range(102, 107):
	if i < 10:
		nome_arquivo = 'Exercicio00' + str(i) + '.py'
		open(nome_arquivo,'x')
	elif i < 100:
		nome_arquivo = 'Exercicio0' + str(i) + '.py'
		open(nome_arquivo,'x')
	else:
		nome_arquivo = 'Exercicio' + str(i) + '.py'
		open(nome_arquivo,'x')