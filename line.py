def line():

A = float(input("Ingrese el coheficiente A:"))
B = float(input("Ingrese el coheficiente B:"))
X1 = float(input("Ingrese el coheficiente X1:"))
X2 = float(input("Ingrese el coheficiente X2:"))

print(f"El coeficiente A de su ecuación de la recta es: {A}")
print(f"El coeficiente A de su ecuación de la recta es: {B}")
print(f"El coeficiente A de su ecuación de la recta es: {X1}")
print(f"El coeficiente A de su ecuación de la recta es: {X2}")

print("\nPara la siguiente ecuación:")
print(f"\tY = {A}X + {B}\n")

Y1 = A*X1 + B
Y2 = A*X2 + B

print("Dados los siguientes puntos:")
print(f"\tP1 ({X1},{Y1})")
print(f"\tP2 ({X2},{Y2})")

d=float((X1-X2)**1/2 + (Y1-Y2)**1/2)

print(f"\nLa distancia entre ellos es: {d}")
