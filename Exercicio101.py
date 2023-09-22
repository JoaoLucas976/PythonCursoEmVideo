def voto(nasc):
    from datetime import datetime
    idade = datetime.today().year - nasc
    if idade < 16:
        return f"Você possui {idade} anos: Não pode votar"
    if (16 <= idade < 18) or idade > 65:
        return f"Você possui {idade} anos: Voto não obrigatório"
    else:
        return f"Você possui {idade} anos: Voto obrigatório"


print(voto(int(input("Insira seu ano de nascimento: "))))
