import numpy as np
import random

#Crear un arreglo bidimensional de 4x4 con elementos de caracteres
arreglo = np.random.choice(list("abcdefghijklmnopqrstuvwxyz"),(4,4))
print(f"Arreglo: \n{arreglo}")

#Contar la cantidad de vocales
cantidadVocales = 0

for i in range(arreglo.size):
    if arreglo.flat[i] in "aeiou":
        cantidadVocales += 1

print(f"Cantidad de vocales: {cantidadVocales}")