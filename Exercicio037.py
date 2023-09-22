numero = int(input("Insira um numero inteiro qualquer: "))
opcao = int(input("Escolha uma base de conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n"))

if opcao == 1:
    print(f"O número {numero} em binário é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O numero {numero} em octal é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O numero {numero} em hexadecimal é {hex(numero)[2:]}")
else:
    print("Escolha uma opção válida !!!")