from datetime import date

ano_nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = date.today().year
diferenca = ano_atual - ano_nascimento

if diferenca <= 9:
    print("Sua categoria é: MIRIM")
elif diferenca > 9 and diferenca <= 14:
    print("Sua categoria é: INFANTIL")
elif diferenca > 14 and diferenca <= 19:
    print("Sua categoria é: JUNIOR")
elif diferenca > 19 and diferenca <= 25:
    print("Sua categoria é: SÊNIOR")
else:
    print("Sua categoria é: MASTER")
