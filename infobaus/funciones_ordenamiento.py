import re
ruta = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\Insumos.csv - Hoja 1.csv"
def leer_csv(ruta:str)->list:
    #Resumen:
    #     Función que abre el archivo en modo de lectura
    #     Solo tiene como parametros a 'ruta' que contiene el path del archivo csv
    #     Su return nos devuelve todo el archivo csv en formato lista
    persona = []
    with open(ruta,'r',encoding='UTF-8') as archivo:
        for linea in archivo:
            persona.append(linea.strip("\n"))
    return persona

#1
def listar_lineas(listado:list):
    #Resumen:
    #     Función que convierte cada insumo en una lista y sus datos en items de la misma. 
    #     Cada dato es separado usando las comas como parametro.
    #     Solo tiene como parametros a 'listado', que es del tipo list. Contiene todo el archivo csv.
    #     Su return nos devuelve una lista cuyos items son listas con los datos de los insumos.
    lista_linea = []
    for dato in listado:
        filas_datos = dato.replace('"',"").split(",")
        lista_linea.append(filas_datos)
    lista_linea.pop(0)
    for linea in lista_linea:
        if linea[2] == " Samsung":
            linea[2] = "Samsung"
    return lista_linea

#2
def lista_cantidad_marca(datos_insumos:list):
    #Resumen:
    #     Función que convierte la lista de insumos en un diccionario que muestra las marcas y su cantidad de insumos
    #     Solo tiene como parametros a 'datos_insumos', que es una lista
    #     Su return nos devuelve un diccionario cuyas keys son las marcas de los insumos y sus valores son la cantidad de veces
    #     que aparecen en el csv.
    marcas = {}
    for insumo in datos_insumos:
        if insumo[2] in marcas:
            marcas[insumo[2]] += 1
        else:
            marcas[insumo[2]] = 1
    return marcas

#3
def listar_insumos_marca(diccionario:dict,datos_insumos:list):
    #Resumen:
    #     Función que convierte la lista de insumos en un diccionario que muestra las marcas y su cantidad de insumos.
    #     Tiene como parametros a 'datos_insumos', que es una lista y a 'diccionario' que es el diccionario de marcas.
    #     Printea la marca del insumo y debajo, los productos y el precio de los productos de esa marca.
    for marca in diccionario:
        print(f"{marca}: ")
        for linea in datos_insumos:
            if marca in linea:
                print(f"    Nombre: {linea[1]}///Precio: {linea[3]} ")

#4
def listar_insumos_caracteristica(dato_usuario:str,datos_insumos:list):
    #Resumen:
    #     Función que con utiliza una característica que ingresa el usuario y devueve todos los productos que la tienen.
    #     Tiene como parametros a 'dato_usuario' que es un string que ingresa el usuario y la lista 'datos_insumos'.
    lista_insumos_coincidentes = []
    for linea in datos_insumos:

        # buscar =  re.search(dato_usuario,linea[4])
        # if (buscar):
        if dato_usuario in linea[4]:
            lista_insumos_coincidentes.append(linea[1])
    for producto in lista_insumos_coincidentes:
        print(f"    {producto}")

#5
def lista_de_precios_ordenada(datos_insumos:list):
    #Resumen:
    #     Función que que extrae todos los precios de la lista de insumos y los añade a una lista
    #     Tiene como parametro a la lista 'datos_insumos'.
    #     Retorna una lista con los precios de los productos como items de la misma.
    lista = []
    for linea in datos_insumos:
        item_de_linea = float(linea[3].strip("$"))
        if  item_de_linea not in lista:
            lista.append(item_de_linea)
    return lista

def ordenar_lista_asc_des(lista:list, asc = True):
    #Resumen:
    #     Función que ordena descendentemente o descendentemente una lista
    #     Tiene como parametro a la lista, que es la lista que queremos ordenar y a asc que nos indica,mediante un booleano
    #     si la lista va a ser ascendente o descendente.
    #     Retorna una lista con los precios de los productos como items de la misma.
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            if (asc and lista[i] < lista[j]) or (not asc and  lista[i] > lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

def listar_por_precio(ordenada:list,datos_insumos:list):
    #Resumen:
    #     Función que muestra el precio y todos los insumos que corresponden a ese precio. En caso de que hayan
    #     varios insumos con ese precio, los insumos se ordenan de manera alfabética.
    #     Tiene como parametro a la 'ordenada' que sería la lista con los precios ordenados
    #     si la lista va a ser ascendente o descendente.
    #     Printea los precios y la marca, el id y la primera característica de los insumos que corresponden a ese precio.
    lista_marcas_ordenar = []
    for precio in ordenada:
        precio = str(precio)
        print(precio)
        for linea in datos_insumos:
            for item in linea:
                buscar = re.search(precio,item)
                if (buscar): 
                    caracteristica = linea[4].split("|!*|")
                    lista_marcas_ordenar.append(f"    Marca: {linea[2]}///ID:{linea[0]}///Nombre: {linea[1]}///caracteristica: {caracteristica[0]}")
        lista_alfabetica = ordenar_lista_asc_des(lista_marcas_ordenar,False)
        for insumo in lista_alfabetica:
            print(insumo)
        lista_marcas_ordenar.clear()