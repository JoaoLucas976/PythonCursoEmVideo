from math import sin,cos,tan, radians

angulo = float(input("Insira um valor de angulo: "))
ang_rad = radians(angulo)
print("O seno de {} é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}".format(angulo, sin(ang_rad), cos(ang_rad), tan(ang_rad)))
