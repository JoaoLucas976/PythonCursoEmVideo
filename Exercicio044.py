print("{:=^40}".format('\033[0;31mLOJINHA DO JÂOJÂO\033[m'))
preco = float(input("Insira o valor do produto: "))
condicao = int(input("Escolha a forma de pagamento:\n[1] A vista\n[2] A vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão\n"))

if condicao == 1:
    print("Você escolheu a opção: A vista")
    print("Seu produto terá 10% de desconto, ficando por R${:.2f}".format(preco*0.9))
elif condicao == 2:
    print("Você escolheu a opção: A vista no cartão")
    print("Seu produto terá 5% de desconto, ficando por R${:.2f}".format(preco*0.95))
elif condicao == 3:
    print("Você escolheu a opção: Em até 2x no cartão")
    print("Seu produto não terá desconto, ficando por R${:.2f}\nCada parcela custará R${:.2f}".format(preco, preco/2))
elif condicao == 4:
    print("Você escolheu a opção: 3x ou mais no cartão")
    totparcelas = int(input("Em quantas vezes você deseja parcelar ? "))
    print("Seu produto terá 20% de juros, ficando por R${:.2f}\nCada parcelar custará R${:.2f}".format(preco*1.2, (preco * 1.2)/totparcelas))
else:
    print("Escolha uma opção válida !!!")
