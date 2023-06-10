import numpy as np
import random

arreglo = np.random.randint(0,1000,10)
print(f"Arreglo: \n{arreglo}")

#Contar los elementos pares del arreglo
contPares = 0

for i in range(arreglo.size):
    if arreglo[i] % 2 == 0:
        contPares += 1

print(f"La cantidad de numeros pares es: {contPares}")

#Suma los elementos impares del arreglo
sumaImpares = 0

for i in range(arreglo.size):
    if arreglo[i] % 2 != 0:
        sumaImpares += arreglo[i]

print(f"La suma de los numeros impares es: {sumaImpares}")

#Mostrar los numeros primos del arreglo
for i in range(arreglo.size):
    contDivisores = 0
    
    for j in range(1,arreglo[i]+1):
        if arreglo[i] % j == 0:
            contDivisores += 1
    if contDivisores == 2:
        print(f"El numero {arreglo[i]} es primo")

