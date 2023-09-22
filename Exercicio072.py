tupla = ("zero","um","dois","três","quatro","cinco",
         "seis","sete","oito","nove","dez","onze","doze",
         "treze","quatorze","quinze","dezesseis","dezessete",
         "dezoito","dezenove","vinte")
n = int(input("Insira um número inteiro [entre 0 e 20]: "))
while n > 20 or n < 0:
    print("Número inválido")
    n = int(input("Insira um número inteiro [entre 0 e 20]: "))
print(f"Você digitou o número {tupla[n]}")
