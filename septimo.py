def mas_grande_mas_pequeno(numeros):
    grande = max(numeros)
    pequeno = min(numeros)
    return grande, pequeno

lista = [5, 20, 40, 1, 15]
numero_mayor, numero_menor = mas_grande_mas_pequeno(lista)

print("El numero mayor de la lista es: ", numero_mayor, " y el numero menor es: ", numero_menor)