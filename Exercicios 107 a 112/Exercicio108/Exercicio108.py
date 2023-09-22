import moeda

n = float(input("Digite o valor: R$"))
print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}")
print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}")
print(f"Aumentando 10% de {moeda.moeda(n)} temos {moeda.moeda(moeda.aumentar(n, 10))}")
print(f"Diminuindo 10% de {moeda.moeda(n)} temos {moeda.moeda(moeda.diminuir(n, 10))}")
