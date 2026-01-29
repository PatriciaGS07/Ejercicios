d={}    #diccionarios co llaves
print(type(d))
d["a"]=10; d["b"]=20; d["c"]=30
print("Diccionario inicial:", d)
# Acceder a un valor por clave
valor_a = d["a"]
print("Valor asociado a la clave 'a':", valor_a)
# Modificar un valor por clave
d["b"] = 25
print("Después de modificar la clave 'b':", d)
# Agregar un nuevo par clave-valor
d["d"] = 40
print("Después de agregar la clave 'd':", d)
# Eliminar un par clave-valor por clave
del d["c"]
print("Después de eliminar la clave 'c':", d)
# Obtener todas las claves
claves = d.keys()
print("Claves del diccionario:", list(claves))
# Obtener todos los valores
valores = d.values()
print("Valores del diccionario:", list(valores))
# Obtener todos los pares clave-valor
items = d.items()
print("Pares clave-valor del diccionario:", list(items))
# Verificar si una clave existe en el diccionario
existe_a = "a" in d
print("¿Existe la clave 'a' en el diccionario?:", existe_a)
# Longitud del diccionario
longitud_d = len(d)
print("Longitud del diccionario:", longitud_d)
# Iterar sobre las claves del diccionario
print("Claves en el diccionario:")
for clave in d:
    print(clave)
# Iterar sobre los pares clave-valor del diccionario
print("Pares clave-valor en el diccionario:")
for clave, valor in d.items():
    print(clave, ":", valor)
# Limpiar todos los elementos del diccionario
d.clear()
print("Después de clear():", d)

tupla1=(10,20,30)   #tuplas mutables parentisis, listas corchetes, diccionearios llaves
lista1=["a","b","c"]  #lista inmutable

dict(zip(tupla1,lista1))  #el zip une los valores en clave (tupla) y valor (lista)
print("Diccionario creado con zip:", dict(zip(tupla1,lista1)))
# Crear un diccionario a partir de dos listas usando zip no se asigna a nadie solo se imprime 