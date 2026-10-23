from entradas import *

#1.INGRESAR CADENA

# nombre = ingresar_cadena("Ingrese su nombre: ","ERROR, el nombre debe tener al menos 3 caracteres",3)
# print(f"Su nombre es: {nombre}")

# dato = ingresar_cadena("Ingrese un dato: ")#Por defecto la funcion ingresar_cadena necesita que la cadena tenga al menos UN SOLO CARACTER
# # dato = ingresar_cadena("Ingrese un dato: ","",0)#Si pongo el parametro cantidad_minima en 0, la funcion no emite ningun error, porque no hay posibilidad de que algo salga mal (puedo guardar una cadena vacia)

# print(f"El dato es: {dato}")

# # for vueltas in range(5):
# #     dato = ingresar_cadena("Ingrese un dato: ")#Por defecto la funcion ingresar_cadena necesita que la cadena tenga al menos UN SOLO CARACTER
# #     print(f"El dato es: {dato}")

#2.INGRESAR NOMBRE PROPIO

# nombre = ingresar_nombre_propio("Ingrese su nombre: ","ERROR, el nombre debe tener al menos 3 letras ", "ERROR, el nombre tiene caracteres no adecuados")
# apellido = ingresar_nombre_propio("Ingrese su apellido: ","ERROR, el apellido debe tener al menos 3 letras ", "ERROR, el apellido tiene caracteres no adecuados")

# print(f"{nombre} {apellido}")

#3.INGRESAR NUMERO POSITIVO (VAMOS A INCLUIR AL CERO)

# numero = ingresar_entero_positivo()
# print(f"Su numero es : {numero}")

# opcion = ingresar_entero_positivo("Ingrese su opcion: ","Error, la opcion no puede estar vacia","La opcion no puede ser nagativa o incluir caracteres no numericos")
# print(f"Opcion elegida: {opcion}")

#Quiero pedir una nota de un alumno del 1 al 10

nota = ingresar_entero_rango(1,10,"Ingrese su nota: ","ERROR, la nota no puede estar vacia","ERROR, la nota tiene un formato invalido o es negativa ","ERROR, la nota debe estar entre 1 y 10")

print(f"Su nota es : {nota}")