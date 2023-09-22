# Métodos de teste de tipo

s1 = input("Insira um conteúdo para a variável: ")
print(f"O tipo primitivo desse valor é: {type(s1)}")
print(f"É numérico ? {s1.isnumeric()}")           # Avalia se o conteúdo da variável é numérico
print(f"É alfabético ? {s1.isalpha()}")           # Avalia se o conteúdo da variável é alfabético (letras)
print(f"É alfanumérico ? {s1.isalnum()}")         # Avalia se o conteúdo da variável é alfanumérico (letras e números)
print(f"Está todo em maiúsculo ? {s1.isupper()}")  # Avalia se o conteúdo da variável está em caixa alta
print(f"Está todo em minúsculo ? {s1.islower()}")  # Avalia se o conteúdo da variável está em caixa baixa
print(f"Está capitalizado ? {s1.istitle()}")  # Avalia se o conteúdo da variável está com letras maiúsculas e minusculas
