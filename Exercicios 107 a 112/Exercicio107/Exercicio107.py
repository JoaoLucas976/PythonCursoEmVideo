import moeda

n = float(input("Digite um valor: "))
print(f"O dobro de R${n:.2f} é R${moeda.dobro(n):.2f}")
print(f"A metade de R${n:.2f} é R${moeda.metade(n):.2f}")
print(f"Aumentando 10% de R${n:.2f} temos: R${moeda.aumentar(n, 10)}")
print(f"Diminuinto 10% de R${n:.2f} temos: R${moeda.diminuir(n, 10)}")