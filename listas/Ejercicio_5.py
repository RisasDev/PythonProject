lista = []
numero = int(input("Ingrese un numero: "))

for i in range(10):
    lista.append(numero * (i + 1))

print(f"Lista original: {lista}")

lista_acsendente = lista.copy()
lista_acsendente.sort()

print(f"Lista acsendente: {lista_acsendente}")

lista_descendente = lista.copy()
lista_descendente.sort(reverse=True)

print(f"Lista descendente: {lista_descendente}")
