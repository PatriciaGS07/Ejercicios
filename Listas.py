lista = [10,100, 2, 3, 89,90, -5,-10,100,-5,89]
print("Lista original:", lista)
# Agregar un elemento al final de la lista
lista.append(50)   
print("Después de append(50):", lista)  
# Insertar un elemento en una posición específica
lista.insert(2, 75)
print("Después de insert(2, 75):", lista)
# Eliminar un elemento por valor  
lista.remove(3)
print("Después de remove(3):", lista)
# Eliminar un elemento por índice  (Posición)
del lista[4]     
print("Después de del lista[4]:", lista)
# Ordenar la lista en orden ascendente
lista.sort()
print("Después de sort():", lista)
# Ordenar la lista en orden descendente
lista.sort(reverse=True)
print("Después de sort(reverse=True):", lista)
# Obtener el índice de un elemento
index_89 = lista.index(89)
print("Índice de 89:", index_89)
# Contar cuántas veces aparece un elemento
count_100 = lista.count(100)
print("Cantidad de veces que aparece 100:", count_100)
# Invertir el orden de la lista
lista.reverse()
print("Después de reverse():", lista)
# Copiar la lista
copia_lista = lista.copy()
print("Copia de la lista:", copia_lista)
# Limpiar todos los elementos de la lista
lista.clear()
print("Después de clear():", lista)
print("Copia de la lista después de limpiar la original:", copia_lista)
# Longitud de la copia de la lista
longitud_copia = len(copia_lista)
print("Longitud de la copia de la lista:", longitud_copia) 
# Acceder a un elemento por índice
elemento_indice_2 = copia_lista[2]
print("Elemento en el índice 2 de la copia de la lista:", elemento_indice_2)
# Rebanado de la lista. Extraer parte de los elementos de la lista
rebanado = copia_lista[1:5]
print("Rebanado de la copia de la lista (índices 1 a 4):", rebanado)
# Iterar sobre los elementos de la copia de la lista
print("Elementos en la copia de la lista:")
# cuidar la identación  (Sangrado, tabulador)
for elemento in copia_lista:
    print(elemento)
# Sumar todos los elementos de la copia de la lista existe la función Sum
suma_elementos = sum(copia_lista)
print("Suma de todos los elementos en la copia de la lista:", suma_elementos)
# Encontrar el valor máximo y mínimo en la copia de la lista
maximo = max(copia_lista)
minimo = min(copia_lista)
print("Valor máximo en la copia de la lista:", maximo)
print("Valor mínimo en la copia de la lista:", minimo)
#agrega una lista (lista dentro de lista, la lista agregada es un elemento)
copia_lista.append([-1,-2,-3])
print("Después de append([-1,-2,-3]):", copia_lista)
# extend agrega elementos sin ser sublistas
copia_lista.extend([4,5,6])
print("Después de extend([4,5,6]):", copia_lista)

#genera una lista en un rango de 0-4
lista2=list(range(5))
print("Nueva lista2 con range(5):", lista2)

#genera una lista en un rango de 2-10 de 2 en 2
lista3=list(range(2,10,2))
print("Nueva lista3 con range(2,10,2):", lista3)


#genera una lista en un rango de -10 a 15 de 2 en 2
lista4=list(range(-10,15,2))
print("Nueva lista4 con range(-10,15,2):", lista4)