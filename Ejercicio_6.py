import random

lista = []

for i in range(10):
    random_number = random.randint(1, 100)
    lista.append(random_number)

lista.sort()

numero_menor = lista[0]
numero_mayor = lista[-1]

print(f"Lista: {lista}")
print(f"Numero menor: {numero_menor}")
print(f"Numero mayor: {numero_mayor}")