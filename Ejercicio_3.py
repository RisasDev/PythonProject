lista = []

for i in range(10):
    numero = int(input(f"({i + 1}) Ingrese un numero: "))
    lista.append(numero)

suma = 0

for i in lista:
    suma += i

promedio = suma / len(lista)

print(f"La suma de los numeros ingresados es: {suma}")
print(f"El promedio de los numeros ingresados es: {promedio}")