import numpy as np

arreglo = np.arange(1,101).reshape((10,10))

#Mostrar valores 50 - 99 - 15 - 30 
print(f"Valores: {arreglo[4][9]} - {arreglo[-1][-2]} - {arreglo[1][4]} - {arreglo[2][9]}")

#Mostrar todos los valores de la fila 5
print(f"Valores de la fila 5: {arreglo[5][::]}")

#Mostrar 3 valores de fila 7 usando Slice (misma logica del bidimensional)
print(f"Valores de la fila 7: {arreglo[7][0:3]}")

