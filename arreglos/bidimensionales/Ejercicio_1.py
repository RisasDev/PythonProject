import numpy as np

arreglo = np.arange(1,10).reshape((3,3))
print(f"Matriz 1: \n{arreglo[0,:]}")
print(f"Matriz 2: \n{arreglo[1,:]}")

#Multiplicar las matrices
print(f"Multiplicacion de las matrices: \n{arreglo[0,:]*arreglo[1,:]}")