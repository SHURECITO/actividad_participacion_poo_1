def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
numero_a_convertir = 3
print("El factorial de ",numero_a_convertir, " es ",factorial(numero_a_convertir))
