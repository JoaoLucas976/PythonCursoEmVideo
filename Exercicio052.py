primo = True
num = int(input("Insira um numero inteiro: "))
if num <= 1:
    print("Esse número não é primo")
elif num == 2:
    print("Esse número é primo")
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        print("Esse número é primo ")
    else:
        print("Esse número não é primo ")
