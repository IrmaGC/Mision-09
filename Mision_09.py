#Irma Gómez Carmona
#Funciones que trabajan con listas

def extraerPares(lista): #agrega a la lista los elementos pares de la lista recibida
    listaPares=[]
    for k in lista:  #visita cada elemento de la lista
        if k%2==0: #si es exactamente divisibles entre dos se agrega a la nueva lista
            listaPares.append(k)
    return listaPares


def extraerMayoresPrevio (lista): #agrega en otra lista los valores que son mayores al dígio anterior a éste
    listaMayores=[]
    for k in range (len(lista)-1): #visita cada elemento de la lista
        if lista[k]<lista[k+1]: #si el elemento de la lista actual es menor que el siguiente elemento, el siguiente elemento se agrega a la nueva lista
            listaMayores.append(lista[k+1])
    return listaMayores


def intercambiarParejas (lista): #intercambia de posición los números de 2 en 2
    listaNueva=[]
    if len(lista)%2==0: #si el número de datos es par
        for k in range (0,len(lista)-1,2): #inicia en 0, pero visita los elementos de 2 en 2
            # en la nueva lista se va a agregar primer el segundo valor, y liego el anterior
            listaNueva.append(lista[k+1])
            listaNueva.append(lista[k])
    #cuando la lista es impar
    else:
        if len(lista)>1: #cuando la lista es mayor a 1 elemento
            for k in range (0,len(lista)-2,2): #visita la lista de 2 en 2 elementos
                # en la nueva lista se va a agregar primer el segundo valor, y liego el anterior
                listaNueva.append(lista[k+1])
                listaNueva.append(lista[k])
        #se agrega a la lista nueva el ultimo elemento (el cual no se intercambia)
        listaNueva.append(lista[-1])
    return listaNueva


def intercambiarMM(lista): #en la lista recibida intecambia de ligar el digito mayor y el menor
    #si hay más de un elemento en la lista
    if len(lista)>0:
        #Obtener el elemento mayor y menos de la lista
        mayor=max(lista)
        menor=min(lista)
        for k in range (len(lista)):
            #visita cada elemento de la lista y cuando encuentra el valor que coincide con el valor mayor, termina el ciclo
            if lista[k]==mayor:
                break
        for j in range (len(lista)):
            # visita cada elemento de la lista y cuando encuentra el valor que coincide con el valor menor, termina el ciclo
            if lista[j]==menor:
                break
        lista[k]= menor  #a la posición donde se encuentra el mayor se le asigna el menor
        lista[j]= mayor  #a la posición donde se encuentra el menor se le asigna el mayor

    return lista


def promediarCentro(lista): #promedia los elementos de una lista, excluyendo a al mayor y el menor
    #si hay me dos elementoas en la lista
    if len(lista)>2:
        #obtener el valor mayor y menor de la lista
        mayor=max(lista)
        menor=min(lista)
        #sumar todos los datos y despues restarle el valor mayor y el menor
        suma=sum(lista)-mayor-menor
        #se divide la suma entre el total de elementos menos 2
        promedio= int(suma/(len(lista)-2))
        return promedio
    else:
    #si hay 2 o menos elementos regresa 0
        return 0


def calcularEstadistica(lista): #calcula la media y la desviación estandar
    mean=0
    desviation=0
    sumDesviation=0
    numDatos = len(lista)
    if numDatos>1:
        #media es la sumatoria de todos los elementos entre el número de elementos en la lista
        mean = sum(lista) / numDatos
        #calcular desviación
        for k in lista:
            sumDesviation+=(k-mean)**2
            desviation=(sumDesviation/(numDatos-1))**0.5
    return mean,desviation  #regresa dupla


def calcularSuma(lista):
    #suma los elementos de un lista, pero no considera como sumandos el 13 y los elementos a sus extremos
    suma=0
    if len(lista)>1:
        for k in range (0,len(lista)):
            if k==0: #primer elemento
                #si el elemento siguiente es 13 o el actual es 13, continuar con el ciclo sin sumar
                if lista[1]==13 or lista[0]==13:
                    continue
            elif k==len(lista)-1: #ultimo elemento
                # si el elemento anterior es 13 o el actual es 13, continuar con el ciclo sin sumar
                if lista[k-1]==13 or lista[k]==13:
                    continue
            elif k>0 and k<len(lista)-1: #los demás elementos
                # si el elemento siguiente o anteriores es 13 o el actual es 13, continuar con el ciclo sin sumar
                if lista[k+1]==13 or lista[k-1]==13 or lista[k]==13:
                    continue
            suma+=lista[k] #si no aplican los casos anteriores se suman los valores
    #si solo hay un elemento en la lista
    elif len(lista)==1:
        if lista[0]==13: #si es 13 regresa 0
            return suma
        else:
            suma=lista[0] #regresa el mismo número
    return suma



