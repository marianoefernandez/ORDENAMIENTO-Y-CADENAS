from constastes import *

def contar_caracter(cadena:str,caracter:str) -> int:
    #Validar los datos de entrada segun corresponda
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            contador += 1

    return contador

def convertir_minuscula(cadena_original:str) -> str:
    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter_original = cadena_original[i]
        caracter_ascii = ord(caracter_original)
        if verificar_mayuscula(caracter_ascii):#Si es mayuscula
            caracter_minuscula = chr(caracter_ascii + 32)
            cadena_copia += caracter_minuscula
        else:
            cadena_copia += caracter_original

    return cadena_copia

def convertir_mayuscula(cadena_original:str) -> str:
    pass

def convertir_titulo(cadena_original:str) -> str:
    #mariano --> "Mariano"
    #mARIANO --> "Mariano"
    #MARIANO --> "Mariano"
    #juan CRUZ --> Juan Cruz
    pass

def normalizar_minuscula(lista_caracteres:list) -> bool:
    if verificar_array_cadenas(lista_caracteres):
        for i in range(len(lista_caracteres)):
            lista_caracteres[i] = eliminar_espacios(lista_caracteres[i])
            lista_caracteres[i] = convertir_minuscula(lista_caracteres[i])
        return True
    else:
        return False

def normalizar_nombre(lista_caracteres:list) -> bool:
    if verificar_array_cadenas(lista_caracteres):
        for i in range(len(lista_caracteres)):
            lista_caracteres[i] = eliminar_espacios(lista_caracteres[i])
            lista_caracteres[i] = convertir_titulo(lista_caracteres[i])
        return True
    else:
        return False

def contar_letras(cadena:str) -> int:
    contador = 0

    if verificar_cadena(cadena):
        cadena = convertir_minuscula(cadena)#Normalizar
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if verificar_minuscula(caracter_ascii):
                contador += 1

    return contador

#Metodo strip casero y mejorado
def eliminar_espacios(cadena_original:str):
    cadena_copia = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == " " and (i == 0 or cadena_original[i - 1] == " "):
            cadena_copia += ""
        else:
            cadena_copia += cadena_original[i]

    if cadena_copia[-1] == " ":#Si el último caracter es un espacio
        cadena_copia = cadena_copia[:-1]#Me elimina el último caracter

    return cadena_copia

def reemplazar_caracteres(cadena_original:str,caracter_reemplazar:str,reemplazo:str) -> str:
    cadena_copia = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == caracter_reemplazar:
            cadena_copia += reemplazo
        else:
            cadena_copia += cadena_original[i]

    return cadena_copia

def verificar_es_alfabetico(cadena:str) -> bool:
    if verificar_cadena(cadena):
        cadena = convertir_minuscula(cadena)#Normalizar (llevar la cadena a un solo formato)

        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_minuscula(caracter_ascii):
                return False

        return True
    else:
        return False

def verificar_es_nombre_propio(cadena:str) -> bool:
    if verificar_cadena(cadena):
        cadena = convertir_minuscula(cadena)#Normalizar (llevar la cadena a un solo formato)

        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_minuscula(caracter_ascii) and caracter_ascii != 32:
                return False

        return True
    else:
        return False

def verificar_es_entero(cadena:str) -> bool:
    #SOLO VERIFICA ENTEROS POSITIVOS O 0
    #PARA EL TP O PARA SP esta funcion verifique tambien los negativos, necesito jugar con la algoritmia para lograr esto.
    #Tratar de que funcione tambien con enteros negativos por ejemplo
    #-10
    #-1
    #-100
    #Consejo --> Aca hay dos escenarios 
    #Escenario 1 --> Cuando es el primer caracter (puede ser numerico o un guion (-))
    #Escenario 2 --> Cuando no es el primer caracter (Solo debe ser numerico)
    #Escenario 3 --> Cuando el primer caracter es un guion, tiene que tener un numero al lado
    if verificar_cadena(cadena):
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_numero(caracter_ascii):
                return False

        return True
    else:
        return False

def verificar_numero(caracter_ascii:int) -> bool:
    return caracter_ascii >= 48 and caracter_ascii <= 57

def verificar_mayuscula(caracter_ascii:int) -> bool:
    return (caracter_ascii >= 65 and caracter_ascii <= 90) or caracter_ascii == 209

def verificar_cadena(cadena:str) -> bool:
    return type(cadena) == str and len(cadena) > 0

def verificar_minuscula(caracter_ascii:int) -> bool:
    return (caracter_ascii >= 97 and caracter_ascii <= 122) or caracter_ascii == 241

def validar_numerico(elemento:any) -> bool:
    return type(elemento) == int or type(elemento) == float

def verificar_array(array:list) -> bool:
    return type(array) == list and len(array) > 0

def verificar_array_numerico(array:list) -> bool:
    #Las listas generalmente no se devuelven, solamente voy a retornar una lista cuando la funcion cree una lista nueva o cuando la funcion copie una lista
    if verificar_array(array):
        for i in range(len(array)):
            if not validar_numerico(array[i]):
                return False

        return True
    else:
        return False

def verificar_array_cadenas(array:list) -> bool:
    if verificar_array(array):
        for i in range(len(array)):
            if not verificar_cadena(array[i]):
                return False

        return True
    else:
        return False


#FUNCIONES DE ORDENAMIENTO

def ordenar_array_numerico_menor_mayor(lista_numeros:list) -> bool:
    if verificar_array_numerico(lista_numeros):
        for izq in range(len(lista_numeros) - 1):
            for der in range(izq + 1,len(lista_numeros)):
                if lista_numeros[izq] > lista_numeros[der]:
                    intercambiar_array(lista_numeros,izq,der)
        return True
    else:
        return False

def ordenar_array_numerico_mayor_menor(lista_numeros:list) -> bool:
    if verificar_array_numerico(lista_numeros):
        for izq in range(len(lista_numeros) - 1):
            for der in range(izq + 1,len(lista_numeros)):
                if lista_numeros[izq] < lista_numeros[der]:
                    intercambiar_array(lista_numeros,izq,der)
        return True
    else:
        return False

def ordenar_array_numerico(lista_numeros:list,criterio:bool = ASC):
    #La funcion se va a encargar de ordenar un array numerico teniendo en cuenta un criterio que se elija, siendo el por defecto, el criterio Ascendente (menor a mayor) --> True
    if verificar_array_numerico(lista_numeros):
        for izq in range(len(lista_numeros) - 1):
            for der in range(izq + 1,len(lista_numeros)):
                if criterio == ASC and lista_numeros[izq] > lista_numeros[der]:
                    intercambiar_array(lista_numeros,izq,der)
                elif criterio == DESC and lista_numeros[izq] < lista_numeros[der]:
                    intercambiar_array(lista_numeros,izq,der)
        return True
    else:
        return False

def ordenar_array_caracteres(lista_caracteres:list,criterio:bool = ASC):
    #ASC --> [A-Z]
    #DESC --> [Z-A]
    if verificar_array_cadenas(lista_caracteres):
        for izq in range(len(lista_caracteres) - 1):
            for der in range(izq + 1,len(lista_caracteres)):
                if criterio == ASC and lista_caracteres[izq] > lista_caracteres[der]:
                    intercambiar_array(lista_caracteres,izq,der)
                elif criterio == DESC and lista_caracteres[izq] < lista_caracteres[der]:
                    intercambiar_array(lista_caracteres,izq,der)
        return True
    else:
        return False

def ordenar_array(array:list,criterio:bool = ASC, tipo:bool = NUMERICO): #--> Que me permita ordenar tanto un array numerico como un array de cadenas
    pass


def intercambiar_array(lista:list,izq:int,der:int) -> None:
    aux_izq = lista[izq]
    lista[izq] = lista[der]
    lista[der] = aux_izq

# lista_datos = [3,5,2,1,14,22,3]
# ordenar_array_numerico_menor_mayor(lista_datos)
# print(lista_datos)