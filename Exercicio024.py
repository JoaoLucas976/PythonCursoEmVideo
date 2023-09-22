nome = input("Insira o nome da sua cidade: ").strip()
nome = nome.lower()
print("Sua cidade começa com santo ? {}".format('santo' in nome[0:5]))
