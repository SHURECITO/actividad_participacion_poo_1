import random

filas = 3
columnas = 4
matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(1, 10))
    matriz.append(fila)
print("Matriz generada:")
for fila in matriz:
    print(fila)
