def mostrar_array(array:list,titulo:str = "",dato:str = ""):
    print(f"{titulo}",end="")
    for i in range(len(array)):
        print(f"{dato} {i + 1}°: {array[i]}")