lista = []

for i in range(3):
    nombre = input(f"({i + 1}) Ingrese un nombre: ")
    lista.append(nombre)

count_nombre_mayor = 0
nombre_mayor = ""

for i in lista:
    cantidad = len(i)

    if count_nombre_mayor < cantidad:
        count_nombre_mayor = cantidad
        nombre_mayor = i

print(f"El nombre con mayor caracteres es {nombre_mayor} con {count_nombre_mayor} caracteres.")