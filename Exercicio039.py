from datetime import date

ano_nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = date.today().year
diferenca = ano_atual - ano_nascimento

if diferenca < 18:
    print(f"Você precisará se alistar daqui a {18 - diferenca} anos")
elif diferenca == 18:
    print("Está na hora de você se alistar")
else:
    print(f"Você deveria ter se alistado a {diferenca - 18} anos atrás")