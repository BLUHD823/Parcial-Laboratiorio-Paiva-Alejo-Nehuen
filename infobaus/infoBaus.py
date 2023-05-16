import re
import json
import csv
ruta_json ="C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\discos.json"
ruta_txt = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\total.txt"
ruta = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\Insumos.csv - Hoja 1.csv"
def leer_csv(ruta:str)->list:
    # Brief:
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
    # Brief:
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
    # Brief:
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
    # Brief:
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
    # Brief:
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
    # Brief:
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
    # Brief:
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
    # Brief:
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

#6
def carrito_de_compras(datos_insumos:list):
    # Brief:
    #     Función que crea una factura de compra en un diccionario. Donde cada producto es una key y sus value es el
    #     total del precio multiplicado la cantidad
    #     Tiene como parametro a la lista 'datos_insumos'
    #     Retorna un diccionario que funciona a modo de factura mostrando todos los productos y el total de cada uno
    respuesta = "Si"
    factura = {}
    while respuesta=="Si":
        producto = input("INGRESE EL NOMBRE DEL PRODUCTO: ")
        cantidad = float(input("INGRESE LA CANTIDAD DEL PRODUCTO QUE QUIERE: "))
        for linea in datos_insumos:
                if producto == linea[1]:
                    precio = float(linea[3].strip("$"))
                    precio_total_producto = cantidad * precio
                    key = linea[1]
                    factura[key] = precio_total_producto
        respuesta = input("¿DESEA SEGUIR INGRESANDO PRODUCTOS?: ")
    return factura

def total_compra(carro_compras:dict):
    # Brief:
    #     Función que hace una suma total de todos los value de cada una de las keys de un diccionario
    #     Tiene como parametro al diccionario 'carro_compras'
    #     Retorna un entero que sería el resultado de la suma total de los value
    suma_total = 0
    for valor in carro_compras.values():
        suma_total  = suma_total + valor
    return suma_total

def porcentaje(total):
    # Brief:
    #     Función que hace el subtotal de los precios de los productos
    #     Tiene como parametro a al str 'total'
    #     Retorna el resultado del impuesto, ingresado por el usuario, multiplicado por el total de los precios
    impuesto = int(input("INGRESE EL PORCENTAJE DEL IMPUESTO: "))
    impuesto = impuesto/100
    sub_total = total - (total * impuesto)
    sub_total = round(sub_total,3)
    return sub_total

def modificar_txt(ruta_txt:str,carro_compras:dict,total:float,sub_total:float):
    # Brief:
    #     Función que escribe en un archivo txt, cada una de las compras, el total y el subtotal de los precios.
    #     Tiene como parametro a la ruta 'ruta_txt' del archivo de texto. Luego tiene al diccionario 'carro_compras'
    #     donde están los productos y sus precios.Luego está el 'total' que es el resultado de la suma de todos los precios
    #     y por último el subtotal que es la multiplicación del total por el porcentaje de impuestos.
    with open(ruta_txt,'w+', encoding='UTF-8') as file:
        file.write(f"FACTURA: \n")
        for key,value in carro_compras.items():
            file.write(f"    Producto: {key}    Precio: {value} \n")
        file.write(f"\n    El total de la compra es: {total}")
        file.write(f"\n    El subtotal de la compra es: {sub_total}")
#7

def guardar_disco_duro(datos_insumos:list):
    # Brief:
    #     Función que escribe busca en la lista de insumos si algún nombre de producto coincide con "Disco Duro", en caso
    #     de que coincidan guarda el nombre y el id en un diccionario.
    #     Tiene como parametro a la lista 'datos_insumos'.
    #     Retorna el diccionario que tiene como keys a los productos que coinciden con Disco Duro.
    product = "Disco Duro"
    dict_disco = {}
    contador = 0
    for linea in datos_insumos:
        if product in linea[1]:
            contador += 1
            dict_disco[contador] = linea[1]
    return dict_disco

def archivo_json(ruta_json:str,dict_disco:dict):
    # Brief:
    #     Función que abre el archivo json y escribe la información del diccionario de Disco Duro.
    #     Tiene como parametro a la ruta del archivo json donde se escribirán el diccionario.
    #     También tiene como parametro al diccionario donde están guardados los discos.
    with open(ruta_json,'w+', encoding='UTF-8') as file:
        json.dump(dict_disco,file,indent=4)

8#
def leer_archivo_json(ruta_json:str):
    # Brief:
    #     Función que abre el archivo json y trae los datos del mismo, en forma de lista.
    #     Tiene como parametro a la ruta del archivo json donde se ubican los discos.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    lista_json  = []
    with open(ruta_json,'r',encoding='UTF-8') as file:
        insumos = json.load(file)
        for key,value in insumos.items():
            key = str(key)
            item = (f"{key}: {value}")
            lista_json.append(item)

    return lista_json

#9

def inflacion(lista:list):
    # Brief:
    #     Función que abre que abre una lista, y se fija si alguno de sus items contiene el signo '$'
    #     en caso de que lo tenga le hace un aumento del  del 8,4%.
    #     Tiene como parametro a una lista.
    #     Retorna un string compuesto del resultado del aumento concatenado con el signo '$'
    multiplicacion = 0
    if "$" in lista:
        numero = float(lista.strip("$"))
        multiplicacion = numero+(numero*0.084)
        multiplicacion = "$"+str(multiplicacion)
    return multiplicacion

def inflacion_lista(datos_insumos:list):
    # Brief:
    #     Función que abre que crea una lista en la que los precios tienen un aumento del 8,4%
    #     Tiene como parametro a la lista 'datos_insumos'.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    for linea in datos_insumos:
        calculo = list((map(inflacion,linea)))
        linea[3] = calculo[3]
    return datos_insumos


def reemplazar_csv(ruta:str,lista_inflacionaria:list):
    # Brief:
    #     Función que abre sobreescribe el archivo csv de insumos con los precios actualizados a la inflación de m
    #     Tiene como parametro a la ruta del archivo json donde se ubican los discos.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    with open(ruta,'w+',encoding='UTF-8', newline="") as file:
        escritura = csv.writer(file)
        for linea in lista_inflacionaria:
            escritura.writerow(linea)


def menu():
    eleccion = 0
    while eleccion != 10:
        print("-----------------------------------------")
        print("-----------------------------------------")
        print("                 MENU                    ")
        print("-----------------------------------------")
        print("1-TRAER DATOS DESDE ARCHIVO. ")
        print("2-LISTAR CANTIDAD POR MARCA. ")
        print("3-LISTAR INSUMOS POR MARCA. ")
        print("4-BUSCAR INSUMO POR CARACTERÍSTICA. ")
        print("5-LISTAR INSUMOS ORDENADOS: ")
        print("6-REALIZAR COMPRAS. ")
        print("7-GUARDAR JSON. ")
        print("8-LEER JSON. ")
        print("9-ACTUALIZAR PRECIOS. ")
        print("10-SALIR DEL PROGRAMA. ")
        eleccion = int(input("INGRESE SU RESPUESTA: "))
        match eleccion:
            case 1:
                listado = leer_csv(ruta)
                datos_insumos = listar_lineas(listado)
                for linea in datos_insumos:
                    print(linea)
            case 2:
                diccionario_marcas = lista_cantidad_marca(datos_insumos)
                for key, value in diccionario_marcas.items(): 
                    print(f"{key}:{value}")
            case 3: 
                listar_insumos_marca(diccionario_marcas,datos_insumos)
            case 4: 
                dato_usuario = input("INGRESE LA CARACTERÍSTICA DEL PRODUCTO: ")
                listar_insumos_caracteristica(dato_usuario,datos_insumos)
            case 5:
                lista_precios = lista_de_precios_ordenada(datos_insumos)
                ordenada = ordenar_lista_asc_des (lista_precios, True)
                listar_por_precio(ordenada,datos_insumos)
            case 6:
                carro_compras = carrito_de_compras(datos_insumos)
                for compra in carro_compras.items():
                    print(compra)
                total = total_compra(carro_compras)
                sub_total = porcentaje(total)
                modificar_txt(ruta_txt,carro_compras,total,sub_total)
            case 7:
                dict_disco = guardar_disco_duro(datos_insumos)
                archivo_json(ruta_json,dict_disco)
            case 8:
                lista_json = leer_archivo_json(ruta_json)
                for item in lista_json:
                    print(f"    {item}")
            case 9:
                lista_inflacionaria = inflacion_lista(datos_insumos)
                reemplazar_csv(ruta,lista_inflacionaria)
menu()

