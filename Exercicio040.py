n1 = float(input("Insira o valor da sua primeira nota: "))
n2 = float(input("Insira o valor da sua segunda nota: "))
media = (n1 + n2)/2
print(f"Sua média é {media}")
if media < 5:
    print("Você foi \033[31mREPROVADO\033[m")
elif media >= 5 and media <= 6.9:
    print("Você está de \033[33mRECUPERAÇÂO\033[m")
else:
    print("Você foi \033[32mAPROVADO\033[m")
