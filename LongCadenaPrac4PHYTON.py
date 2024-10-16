def conteo(tipodecadena):
    t = 0  
    n = len(tipodecadena)  
    i = 0 
    
    while i < n:
        if tipodecadena[i] == '(':  
            for j in range(i + 1, n):
                if tipodecadena[j] == ')':  
                    t += 2 
                    i = j  
                    break   
        i += 1

    return t


n = int(input("Ingresa el tamaño de la cadena: "))
cadena_ingresada = input("Ingresa la cadena: ")


tamanio = conteo(cadena_ingresada)
print(f"El número de caracteres válidos es: {tamanio}")