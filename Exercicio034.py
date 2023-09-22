salario = float(input("insira o valor do seu salário: "))
if salario > 1250:
    novo = 1.10*salario
else:
    novo = 1.15*salario
print("Seu novo salário será R${:.2f}".format(novo))