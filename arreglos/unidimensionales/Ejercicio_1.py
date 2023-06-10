import numpy as np
import random

arregloA = np.random.randint(0,500,(100))
print(arregloA)

#Mostrar los numeros pares del arreglo
for i in range(arregloA.size):
    if i % 2 == 0:
        print(f"El indice {i} es par")

#Mostrar el numero mayor del arreglo
print(f"El numero mayor del arreglo es: {arregloA.max()}")


#Mostrar el indice del numero mayor del arreglo
indiceMayor = 0

for i in range(arregloA.size):
    if i > indiceMayor:
        indiceMayor = i

print(f"El indice del numero mayor es: {indiceMayor}")

#Mostrar el numero menor del arreglo
print(f"El numero menor del arreglo es: {arregloA.min()}")

#Copiar el arreglo y multiplicarlo por 3
copyArregloA = arregloA.copy()
copyArregloA *= 3
print(f"Arreglo multiplicado por 3: \n{copyArregloA}")

#Mostrar la suma de los elementos del arreglo
print(f"La suma de los elementos del arreglo es: {arregloA.sum()}")

#Mostrar el promedio de los elementos del arreglo
print(f"El promedio de los elementos del arreglo es: {arregloA.mean()}")