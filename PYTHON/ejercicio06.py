#ingrese un numero  y digo si es par o inpar
#pedir al usuario ingresar un numero
#calculo (variable % 2 == es par)

"""
dotstring
cuando es comillas de saltos de lineas
"""
numero=int(input("INGRESE UN NUMERO \t"))
if numero==0:
    print("cero")
elif (numero % 2 == 0):
    print("es par")
else:
    print("es impar")