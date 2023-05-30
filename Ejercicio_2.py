lista = []

while True:
    try:
        numero = int(input("Ingrese un numero: "))

        if numero == 0:
            break
        else:
            lista.append(numero)
            print(f"Se añadio el numero {numero} a la lista")
    except ValueError:
        print("No es un numero valido")

lista.sort()
print(lista)