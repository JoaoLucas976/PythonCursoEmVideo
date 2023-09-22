from math import hypot

cat_oposto = float(input("Insira o valor do cateto oposto: "))
cat_adjascente = float(input("Insira o valor do cateto adjascente: "))
hipotenusa = hypot(cat_adjascente, cat_oposto)
print("O valor da hipotenusa é {:.2f}".format(hipotenusa))
