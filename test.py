lista = []
partes = ["867961-B21", "840369-A21", "777876-H55-H6"]

def grabarParte():
    numero_parte = input("Ingrese numero el parte: ")

    if partes.__contains__(numero_parte):
        nombre_producto = input("Ingrese nombre del producto: ")

        if len(nombre_producto) >= 6:
            precio_producto = int(input("Ingrese precio del producto: "))

            if precio_producto > 0:
                producto = [numero_parte, nombre_producto, precio_producto]
                lista.append(producto)
                print(f"El producto '{nombre_producto}' se ha grabado correctamente.")
            else:
                print(f"El precio del producto tiene que ser mayor a cero.")
        else:
            print(f"El nombre del producto '{nombre_producto}' debe contener minimo 6 caracteres.")
    else:
        print(f"El numero del parte '{numero_parte}' no es valido.")

def buscarParte():
    numero_parte = input("Ingrese el numero de parte a buscar: ")

    if partes.__contains__(numero_parte):
        for producto in lista:
            if producto[0] == numero_parte:
                print(f"Numero de parte: {producto[0]}")
                print(f"Nombre del producto: {producto[1]}")

                precio_producto = producto[2]

                if precio_producto > 500:
                    print(f"Precio del producto: {precio_producto}")
                else:
                    print(f"Precio del producto: Sin Stock")

    else:
        print(f"El numero de parte '{numero_parte}' no existe.")

def imprimirParte():
    for producto in lista:
        print(f"Numero de parte: {producto[0]}")
        print(f"Nombre del producto: {producto[1]}")
        print(f"Precio del producto: {producto[2]}")
        print("")

while True:
    print("Menu Principal")
    print("1. Grabar Parte")
    print("2. Buscar Parte")
    print("3. Imprimir Partes")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        grabarParte()
    elif opcion == 2:
        buscarParte()
    elif opcion == 3:
        imprimirParte()
    elif opcion == 4:
        print("Gracias por usar el programa.")
        print("Software desarrollado por: @RisasDev (v1.0)")
        break