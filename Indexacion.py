mascotas="perro gato pez conejo tortuga iguana serpiente caballo oveja cerdo"
print(mascotas)
print("INDEXACIÓN DE CADENAS")
print("-"*30)
lista_mascotas=mascotas.split(" ")
print(lista_mascotas)
print(lista_mascotas[0])
print(lista_mascotas[-1])   # "último"
print(lista_mascotas[2:5])  # Secuencia[inicio:fin]
print(lista_mascotas[:4])   # Secuencia[:fin] ultimos 4
print(lista_mascotas[3:])   # Secuencia[inicio:]
print(lista_mascotas[1:8:2])  # Secuencia[inicio:
print(lista_mascotas[::-1])  # Lista invertida secuencia[inicio:fin:paso]
print(" ".join(lista_mascotas[::-1]))  # Cadena invertida

print("INDEXACIÓN DE LISTAS CON NUMEROS")
print("-"*30)
numeros=[0,10,1,20,2,30,3,40,4]
print(numeros)
print(numeros[::2])  # Secuencia[inicio:fin:paso]
print(numeros[1::2])  # Secuencia[inicio:fin:paso]
print(numeros[::-1])  # Lista invertida secuencia[inicio:fin:paso]
print(sum(numeros[1::2]))  # Suma de los números en posiciones impares

print("DESCIFRANDO PALABRAS SECRETAS")
print("-"*30)
palabra_secreta="8-2^u-j=u@i!o[s&e<c?e>r+y#a&h(o_n"
respuesta=palabra_secreta[::-1] #:: cadena invertida de cero a -1  no se escribe el cero no es necesario
print(respuesta[0::2]) #se imprime de 2 en 2

respuesta2=respuesta[0:2]
print(respuesta2)


#print(respuesta2[0:1:1] + " " + respuesta2[2:5:1]) 
print(respuesta2[0:2:1]+" "+respuesta2[2:5:1]+" "+respuesta2[5:11:1]+" "+respuesta2[11:15:1]+" "+respuesta2[15:17:1])




