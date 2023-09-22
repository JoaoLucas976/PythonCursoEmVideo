nome = input("Insira o seu nome completo: ").strip()
nome_separado = nome.split()
print("Seu primeiro nome é {}\nSeu último nome é {}".format(nome_separado[0],nome_separado[len(nome_separado)-1]))
