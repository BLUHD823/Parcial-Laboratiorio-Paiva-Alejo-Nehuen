import random
ruta = ".\Insumos.csv - Hoja 1.csv"


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

def agregar_elemento(datos_insumos:list):
    #Resumen:
    #     Función que que usando map y lambda agrega a cada insumo de datos_insumos un stock random de entre 0 y 10. 
    #     Solo tiene como parametro a la lista datos_insumos.
    list(map(lambda insumos: insumos.append(random.randint(0,10)),datos_insumos))

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
    bandera = False
    for marca in diccionario:
        print(f"{marca}: ")
    
    while bandera == False:
        marca_usuario = input("INGRESE EL NOMBRE DE LA MARCA: ")
        for marca in diccionario:
            if marca_usuario == marca:
                bandera = True
                print(f"{marca_usuario}: ")
                for linea in datos_insumos:
                    if marca_usuario in linea[2]:
                        print(f"    Nombre: {linea[1]}///Precio: {linea[3]} ")
    

#4
def listar_insumos_caracteristica(dato_usuario:str,datos_insumos:list):
    #Resumen:
    #     Función que con utiliza una característica que ingresa el usuario y devueve todos los productos que la tienen.
    #     Tiene como parametros a 'dato_usuario' que es un string que ingresa el usuario y la lista 'datos_insumos'.
    lista_insumos_coincidentes = []
    for linea in datos_insumos:
        if dato_usuario in linea[4]:
            lista_insumos_coincidentes.append(linea[1])
    for producto in lista_insumos_coincidentes:
        print(f"    {producto}")

#5


def ordenar_lista_asc_des(lista:list, des = True):
    #Resumen:
    #     Función que ordena descendentemente o descendentemente una lista
    #     Tiene como parametro a la lista, que es la lista que queremos ordenar y a asc que nos indica,mediante un booleano
    #     si la lista va a ser ascendente o descendente.
    #     Retorna una lista con los precios de los productos como items de la misma.
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            if (des and lista[i] < lista[j]) or (not des and  lista[i] > lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

def ordenar_diccionario_asc_des(lista:list,key:str,des = True,):
    #Resumen:
    #     Función que ordena descendentemente o descendentemente un diccionario
    #     Tiene como parametro a la lista, que es la lista que queremos ordenar, y la key del diccionario y a asc que nos indica,mediante un booleano
    #     si la lista va a ser ascendente o descendente.
    #     Retorna una lista que está ordenada usando los valores de las key específicada como referencia.
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            if (des and lista[i][key] < lista[j][key]) or (not des and  lista[i][key] > lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

def crear_diccionario(datos_insumos: list):
    #Resumen:
    #     Función que crea una lista en la que se almacenará cada una las lineas, de 'datos_insumos', como un diccionario
    #     Tiene como parametro a la lista de datos insumos
    #     Retorna una lista cuyas lineas son diccionarios que contiene las carácterísticas de cada insumo
    lista_diccionarios = []
    for linea in datos_insumos:
        diccionario ={}
        diccionario['ID'] = linea[0]
        diccionario['Nombre'] = linea[1]
        diccionario['Marca'] = linea[2]
        diccionario['Precio'] = float(linea[3].strip("$"))
        caracteristica = linea[4].split("|!*|")  
        diccionario['Característica'] = caracteristica[0]
        lista_diccionarios.append(diccionario)
    return lista_diccionarios


