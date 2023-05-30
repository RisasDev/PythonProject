lista_nombres = []
lista_apellidos = []

for i in range(3):
    nombre = input(f"({i + 1}) Ingrese un nombre: ")
    lista_nombres.append(nombre)

for i in range(3):
    apellido = input(f"({i + 1}) Ingrese un apellido: ")
    lista_apellidos.append(apellido)

lista_nombres.sort()
lista_apellidos.sort()

print(f"Lista de nombres: {lista_nombres}")
print(f"Lista de apellidos: {lista_apellidos}")