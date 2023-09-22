campbrasi = ("Fluminense", "Flamengo", "Athlético-PR", "Palmeiras", "Botafogo",
             "Bragantino", "Corinthians", "Vasco da Gama", "Grêmio", "Internacional",
             "Fortaleza", "Bahia", "Cruzeiro", "São Paulo", "Atlético-MG", "Cuiabá",
             "Santos", "Goiás", "América-MG", "Coritiba")
print("RESULTADOS CAMPEONATO BRASILEIRO")
print("="*30)
# print(f"Os 5 primeiros colocados são: {campbrasi[0:5]}")
for i in range(0, 5):
    print(f"O {i + 1}º colocado é {campbrasi[i]}")
print("="*30)
# print(f"Os 4 últimos colocados são: {campbrasi[-4:]}")
for i in range(-1, -5, -1):
    print(f"O {21 + i}º colocado é {campbrasi[i]}")
print("=" * 30)
print(f"Os times em ordem alfabética são: {sorted(campbrasi)}")
print("=" * 30)
print(f"O Chapecoense está na {campbrasi.index('Vasco da Gama') + 1}ª posição")
