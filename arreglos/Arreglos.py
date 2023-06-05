import numpy as np

arreglo = np.array([1,2,3,4,5])
print(arreglo)

# ndim: dimensiones del arreglo
print(f"Dimensiones del arreglo: {arreglo.ndim}")

# len(arreglo): longitud del arreglo
print(f"Longitud del arreglo: {len(arreglo)}")

# slice: nos permite obtener un subarreglo
# start: indicamos el indice de inicio
# stop: indicamos el indice de fin
# step: indicamos el salto
# formato: arreglo[start:stop:step]
print(f"Subarreglo: {arreglo[::]}")

# rellenar con for
lista = [i for i in range(1, 11)]
print(lista)

# transformar lista a arreglo
arreglo = np.array(lista)
print(arreglo)

# rellenar con numpy
arreglo = np.arange(1, 11)
print(arreglo)

# operaciones con arreglos
# suma
arreglo += 5
print(arreglo)

# resta
arreglo -= 5
print(arreglo)

# multiplicacion
arreglo *= 5
print(arreglo)

# comparacion
print(arreglo > 10)

# obtener numero mayor
print(arreglo.max())

# obtener numero menor
print(arreglo.min())

# obtener promedio
print(arreglo.mean())

# obtener suma de elementos
print(arreglo.sum())

# bideimensional
arregloBidimensional = np.arange(1, 101).reshape(10, 10)
print(arregloBidimensional[::][::])