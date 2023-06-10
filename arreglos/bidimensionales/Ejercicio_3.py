import numpy as np
import random

arreglo = np.random.randint(0,100,(4,5))
print(f"Arreglo: \n{arreglo}")

#Recorrer el arreglo y mostrar los valores de las filas
for i in range(arreglo.shape[0]):
    print(f"Suma de los valores de la fila {i}: {arreglo[i,:].sum()}")

#Recorrer el arreglo y mostrar los valores de las columnas
for i in range(arreglo.shape[1]):
    print(f"Suma de los valores de la columna {i}: {arreglo[:,i].sum()}")

#Mostrar la suma de los valores de la diagonal principal
print(f"Suma de los valores de la diagonal principal: {arreglo.diagonal().sum()}")

#Mostrar la cantidad de los valores impares
cantidadImpares = 0

for i in range(arreglo.size):
    if arreglo.flat[i] % 2 != 0:
        cantidadImpares += 1

print(f"Cantidad de valores impares: {cantidadImpares}")
