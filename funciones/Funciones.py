lista = []

def listar(lista):
    for i in lista:
        print(i)

def eliminarElemento(lista, elemento):
    lista.remove(elemento)

def agregarElemento(lista, elemento):
    lista.append(elemento)

def calcularSuma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

while True:
    print("Menu de la lista")
    print("1. Listar")
    print("2. Agregar")
    print("3. Eliminar")
    print("4. Calcular Suma")
    print("5. Salir")

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        if lista.__len__() == 0:
            print("La lista esta vacia.")
        else:
            print("Los elementos de la lista son: ")
            print("-------------------------------")
            listar(lista)
            print("-------------------------------")
    elif opcion == 2:
        elemento = int(input("Digite el elemento a agregar: "))
        agregarElemento(lista, elemento)
        print(f"El elemento {elemento} se agrego correctamente.")
    elif opcion == 3:
        elemento = int(input("Digite el elemento a eliminar: "))

        try:
            eliminarElemento(lista, elemento)
            print(f"El elemento {elemento} se elimino correctamente.")
        except:
            print(f"El elemento {elemento} no existe en la lista.")
    elif opcion == 4:
        print(f"La suma de los elementos de la lista es: {calcularSuma(lista)}")
    elif opcion == 5:
        print("Gracias por usar el programa.")
        break
    
    esperar = input("Presione una tecla para continuar...")