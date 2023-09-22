mercado = ("Sabonete", 4.50, "Abacaxi", 6.00, "Batata", 4.00)
print("-=-"*10)
print(f"{'MERCADINHO DO SEU JOÃO':^30}")
print("-=-"*10)
for i in range(0,len(mercado),2):
    print(f"{mercado[i]:.<24}R${mercado[i + 1]:.2f}")
print("-=-"*10)
