total = 0
produtos1000 = 0
preco_barato = 0
nome_barato = ""
while True:
    print("="*20)
    print("CADASTRO DE PRODUTO")
    print("=" * 20)
    nome = input("Insira o nome do produto: ")
    preco = float(input("Insira o preço do produto: "))
    total += preco
    if preco_barato == 0 or preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    if preco > 1000:
        produtos1000 += 1
    continuar = input("Gostaria de continuar [S/N] ? ").upper().strip()
    while continuar not in "SN":
        print("Escolha inválida")
        continuar = input("Gostaria de continuar [S/N] ? ").upper().strip()
    if continuar == "N":
        break
print(f"Sua compra custará R${total:.2f}")
print(f"{produtos1000} produtos custam mais de R$ 1.000,00")
print(f"O produto mais barato é {nome_barato} e ele custa R${preco_barato:.2f}")
