import math

def areacirculo(radio):
    return math.pi * radio**2

radio = float(input("Ingrese el radio del circulo a calcular: "))
area = areacirculo(radio)

print("El valor del area del circulo con radio ",radio," es: ", area)