# Lista inicial de exercícios
lista = [1, 5, 25, 250, 75, 100]
print(f"Inicial: {lista}")

#append(valor): Agregar un elemento al final de la lista
lista.append(250)
print(f"Append: {lista}")

#extend(lista): Agregar una lista al final de la lista
lista.extend([1000, 750, 300])
print(f"Extend: {lista}")

#insert(posicion, valor): Agregar un elemento en una posición específica
lista.insert(3, 999)
print(f"Insert: {lista}")

#remove(valor): Eliminar un elemento de la lista
lista.remove(25)
print(f"Remove: {lista}")

#pop(posicion): Eliminar un elemento de la lista en una posición específica
lista.pop(3)
print(f"Pop: {lista}")

#reverse(): Invertir el orden de la lista
lista.reverse()
print(f"Reverse: {lista}")

#sort(): Ordenar la lista
lista.sort()
print(f"Sort: {lista}")

#sort(reverse=True): Ordena la lista de mayor a menor
lista.sort(reverse=True)
print(f"Sort reverse: {lista}")