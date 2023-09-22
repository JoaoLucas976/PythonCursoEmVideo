from datetime import datetime

maiores = 0
ano_atual = datetime.today().year

for i in range(0, 7):
    ano_nascimento = int(input(f"insira o ano de nascimento da {i+1}a pessoa : "))
    if (ano_atual - ano_nascimento) >= 21:
        maiores += 1
print(f"Existem {maiores} pessoas maiores de idade nesse grupo")
print(f"Existem {7 - maiores} pessoas menores de idade nesse grupo")