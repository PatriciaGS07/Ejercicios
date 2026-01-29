saludo='Hola Mundo'

print("LONGITUD DE CADENAS")
print("-"*30)
longitud=len(saludo)
print(saludo)
print("La longitud de la cadena es:",longitud)

print("-"*30)
print("CADENAS Y CADENAS")
print("-"*30)
cad="Esta es una 'cadena con comillas simples' dentro de comillas dobles"
print(cad)
print(cad[0])
# cad[0]='e'  #Error, las cadenas son inmutables
lenguaje="Python"
descripcion="Este es un buen curso"
frase=descripcion+" de "+lenguaje
print(frase)

print("-"*30)
print("CADENAS Y NUMEROS")
print("-"*30)
total=5500
#mensaje="El total de la compra es: "+total+" pesos"
mensaje="El total de la compra es: "+str(total)+" pesos"
print(mensaje)
mensaje=f"El total de la compra es: {total} pesos"
print(mensaje)

print("-"*30)
print("AGREGAR SALTOS DE LINEAS A CADENAS")
print("-"*30)
mensaje="Orden con 10 elementos\nCargo $5500.99\n¡Gracias por su preferencia!"
print(mensaje)

print("-"*30)
print("FUNCIONES CON CADENAS")
print("-"*30)
nombres="Ana,Maria,Juan,Carlos,Luis"
elementos="a a a b b B c c c c c aa"
print(nombres.upper())
print(nombres.lower())
print(nombres.capitalize())
print(nombres.title())
print(nombres.replace("a","x"))
print(nombres.split(","))
print(nombres.count("a"))
print(elementos.count("a"))
print(nombres.split(",")[0]) 
print(nombres.split(",")[-1]) 
print(nombres.split(",")[-2])
#print(nombres.split(",")[-6])
print(nombres.replace("Juan","Pedro"))
print(nombres.replace(","," "))
print(nombres.endswith("Luis"))
print(nombres.startswith("Ana"))
print(nombres.index("Carlos"))
print(nombres.find("Juan"))

print("-"*30)
print("Cadenas multilínea")
print("-"*30)
texto_multilinea="""Este es un texto
[][]que abarca varias líneas.
**Podemos escribir lo que queramos aquí,
$$y se mantendrá el formato!!."""
print(texto_multilinea)
cadena_limpia=texto_multilinea.replace("[]","")\
    .replace("**","").replace("$$","")
print(cadena_limpia)