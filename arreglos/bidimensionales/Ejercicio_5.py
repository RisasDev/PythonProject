import numpy as np
import random

arreglo = np.arange(1,101).reshape((10,10))

#Mostrar valores 50 - 99 - 15 - 30 
print(f"Valores: {arreglo[4][9]} - {arreglo[-1][-2]} - {arreglo[1][4]} - {arreglo[2][9]}")

#Mostrar todos los valores de la fila 5
print(f"Valores de la fila 5: {arreglo[4][:]}")

#Mostrar 3 valores de fila 7 usando Slice (misma logica del bidimensional)
print(f"Valores de la fila 7: {arreglo[6][0:3]}")

#Parte 4 
#Mostrar los primeros 4 datos de las primeras 5 filas
print(f"Primeros 4 datos de las primeras 5 filas: \n{arreglo[0:5,0:4]}")

#Crear un arreglo bidimensional de 3x3 
#Con datos aleatorios de 0 a 100
arreglo = np.random.randint(0,100,(3,3))
print(f"Arreglo de 3x3: \n{arreglo}")