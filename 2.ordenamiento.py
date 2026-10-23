from funciones import ordenar_array_numerico_menor_mayor, ordenar_array_numerico_mayor_menor,ordenar_array_numerico,ordenar_array_caracteres,normalizar_minuscula,normalizar_nombre
from constastes import *
from salidas import mostrar_array

# lista_numeros = [5,3,1,9,7]

#Menor a mayor --> [1,3,5,7,9]

# print(f"Lista antes --> {lista_numeros}")

#Algoritmo de burbujeo
#1.For principal (los numeros de la izquierda) --> VERDES
# for izq in range(len(lista_numeros) - 1):
#     #2.For secundario (Para los numeros de la derecha) --> ROJO
#     #range tenia 3 parametros
#     #Inicio --> incluyente
#     #Fin --> Excluyente
#     #Incremento
#     for der in range(izq + 1,len(lista_numeros)):
#         if lista_numeros[izq] > lista_numeros[der]:
#             #Intercambiar los valores (swap)
#             #Utilizar una variable auxiliar o temporal para evitar perder ese valor.
#             aux_izq = lista_numeros[izq]
#             lista_numeros[izq] = lista_numeros[der]
#             lista_numeros[der] = aux_izq
#             # lista_numeros[izq],lista_numeros[der] = lista_numeros[der],lista_numeros[izq]#Esto funciona, pero no lo vamos a hacer (PORQUE SI PASAN A OTRO LENGUAJE COMO C, ESTO VA A ROMPER) --> Ademas de que como estamos aprendiendo a programar no es muy didactico y quiero algo más simple

# print(f"Lista despues --> {lista_numeros}")


#Menor a mayor --> [1,3,5,7,9]
lista_numeros = [5,3,1,9,7]
print(f"Lista antes --> {lista_numeros}")
# ordenar_array_numerico_menor_mayor(lista_numeros)
ordenar_array_numerico(lista_numeros)
print(f"Lista despues --> {lista_numeros}")

#Mayor a menor --> [9,7,5,3,1]
# print(f"Lista antes --> {lista_numeros}")
# # ordenar_array_numerico_mayor_menor(lista_numeros)
# ordenar_array_numerico(lista_numeros,DESC)
# print(f"Lista despues --> {lista_numeros}")

#Ordenar un array de [A-Z]

# lista_nombres = [
#     "juan", "MARIA", "  Lucas", "sofia ", "MaTeO",
#     "valentina", "SANTIAGO ", "camila", " tomas", "MARTINA",
#     "benjamin", "  LUCIA  ", "JoAqUiN", "florencia", "nicolas ",
#     " AGUSTINA", "facundo", "JULIETA", "fRANCO", "micaela  "
# ]

#SIEMPRE QUE VAYAN A ORDENAR UNA LISTA DE NOMBRES O DE CARACTERES O DE PALABRAS DEBEN NORMALIZAR LOS DATOS --> LLEVARLOS A UN SOLO FORMATO
# mostrar_array(lista_nombres,"DATOS SIN NORMALIZAR\n","Nombre")

# caracteres_especiales = [
#     "á", "é", "í", "ó", "ú",
#     "Á", "É", "Í", "Ó", "Ú",
#     "ü", "Ü",
#     "ñ", "Ñ"
# ]

# for i in range(len(caracteres_especiales)):
#     print(f"{caracteres_especiales[i]} - {ord(caracteres_especiales[i])}")



#Si ordeno la lista de nombres de menor a mayor [A-Z]

# normalizar_minuscula(lista_nombres)
# print("LISTA DE NOMBRES ANTES")
# mostrar_array(lista_nombres,"NOMBRES\n","Nombre")
# ordenar_array_caracteres(lista_nombres)#Por defecto los ordena de [A-Z]
# print("LISTA DE NOMBRES DESPUES")
# mostrar_array(lista_nombres,"NOMBRES\n","Nombre")

#Si ordeno la lista de nombres de mayor a menor [Z-A]

# print("LISTA DE NOMBRES ANTES")
# mostrar_array(lista_nombres,"NOMBRES\n","Nombre")
# ordenar_array_caracteres(lista_nombres,DESC)#Criterio DESC ordena [Z-A]
# print("LISTA DE NOMBRES DESPUES")
# mostrar_array(lista_nombres,"NOMBRES\n","Nombre")

