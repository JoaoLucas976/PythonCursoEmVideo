nome = input("Insira o seu nome completo: ")
nome_separado = nome.split()
print("Seu nome com maiúsculas é {} \nSeu nome com minúsculas é {}".format(nome.upper(),nome.lower()))
print("O total de letras é: ",len(nome.replace(" ",'')))
print("O primeiro nome é {} e ele tem {} letras".format(nome_separado[0],len(nome_separado[0])))

