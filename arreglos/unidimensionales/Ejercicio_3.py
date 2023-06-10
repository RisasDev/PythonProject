import numpy as np
import random

arregloA = np.random.randint(0,300,10)
arregloB = np.random.randint(0,300,10)

#Mostrar por pantalla las suma de los elementos de cada arreglo
print(f"Suma de los elementos del arreglo A: {arregloA.sum()}")
print(f"Suma de los elementos del arreglo B: {arregloB.sum()}")

#Mostrar por pantalla la suma de los elementos de los arreglos A y B
sumaArreglos = arregloA.sum() + arregloB.sum()
print(f"Suma de los elementos de los arreglos A y B: {sumaArreglos}")

#Mostrar por pantalla la tbla de multiplicar de los elementos impares del arreglo B
for i in range(arregloB.size):
    if arregloB[i] % 2 != 0:
        numeroImpar = arregloB[i]
        print(f"Tabla de multiplicar del numero {numeroImpar}")

        for j in range(1,11):
            print(f"{numeroImpar} x {j} = {numeroImpar*j}")

        print("")