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
cad=cad + "algo"
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
print(nombres.capitalize())      #Primera letra mayuscula  
print(nombres.title())
print(nombres.replace("a","x"))  #Replaza a por x
print(nombres.split(","))        #dividir cada vez que encuentra ,
print(nombres.count("a"))        #contar las a      
print(elementos.count("a"))          
print(nombres.split(",")[0])     #divide cada vez que encuentra , y extrae el elemento 0
print(nombres.split(",")[-1])    # posición de derecha a izq
print(nombres.split(",")[-2])
#print(nombres.split(",")[-6])
print(nombres.replace("Juan","Pedro"))
print(nombres.replace(","," "))
print(nombres.endswith("Luis"))   #si la cadena termina con luis
print(nombres.startswith("Ana"))  #si la cadena inicia con Ana 
print(nombres.index("Carlos"))    #muestra la posicion de carlos (caracteres)
print(nombres.find("Juan"))       #encuentra a juan devuelve la posición (caracteres) 

print("-"*30)
print("Cadenas multilínea")
print("-"*30)
texto_multilinea="""Este es un texto     
[][]que abarca varias líneas.
**Podemos escribir lo que queramos aquí,
$$y se mantendrá el formato!!."""
print(texto_multilinea)  
#concepto sanitizar el texto es decir limpiar 
cadena_limpia=texto_multilinea.replace("[]","")\
    .replace("**","").replace("$$","")
print(cadena_limpia)


print("-"*30)
print("CADENAS FORMATEADAS")
print("-"*30)
nombre="Gabriel"
edad=28
mensaje="Mi nombre es {} y tengo {} años.".format(nombre,edad)     
print(mensaje)
# """ Para hacer multilineas 
mitote="""Para enterarlos que    
el dia de ayer me encontré con {}
que no veía desde que se graduó con {}.
y ahora resulta que ya no vive con {}
el que eras amigo de {}
porque se juntó con {}"""
mitote_completo=mitote.format(*nombres.split(","))  # *Para tener acceso a las listas para trabajar como texto y no lista 
print(mitote_completo)