import moeda

n = float(input("Digite um valor: R$"))
print(f"O dobro de {moeda.moeda(n)} é {moeda.dobro(n, form=True)}")
print(f"A metade de {moeda.moeda(n)} é {moeda.metade(n, form=True)}")
print(f"Aumentando 10% de {moeda.moeda(n)} temos {moeda.aumentar(n, 10, form=True)}")
print(f"Diminuindo 10% de {moeda.moeda(n)} temos {moeda.diminuir(n, 10, form=True)}")
