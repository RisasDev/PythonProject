lista = []

while True:
    nombre = input("Ingrese un nombre: ")
    lista.append(nombre)

    opcion = int(input("¿Desea ingresar otro nombre?\n1) SI\n2) NO\nIngrese una opcion: "))

    if opcion == 2:
        break

count_nombre_menor = 0
nombre_menor = ""

for i in lista:
    cantidad = len(i)

    if cantidad < count_nombre_menor or count_nombre_menor == 0:
        count_nombre_menor = cantidad
        nombre_menor = i

lista.remove(nombre_menor)
print(f"Se elimino el nombre {nombre_menor} de la lista por ser el de menor cantidad de caracteres.")