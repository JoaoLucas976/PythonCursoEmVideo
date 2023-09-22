valor = float(input("Qual o valor da casa ? "))
salario = float(input("Qual o valor do seu salário ? "))
anos = int(input("Em quantos anos você pretende pagar a casa ? "))
prestacao = valor/(anos*12)

if prestacao > 0.3*salario:
    print(f"A prestação será de R${prestacao:.2f} ao mês")
    print("Empréstimo \033[0;31mNEGADO\033[m")
else:
    print(f"A prestação será de R${prestacao:.2f} ao mês")
    print("Empréstimo \033[0;32mAPROVADO\033[m")