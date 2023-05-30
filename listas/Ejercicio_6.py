import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

lista.sort()

numero_menor = lista[0]
numero_mayor = lista[-1]

print(f"Lista: {lista}")
print(f"Numero menor: {numero_menor}")
print(f"Numero mayor: {numero_mayor}")