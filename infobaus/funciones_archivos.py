import csv
import json
import random
import re
#Resumen:
#   Variable que guarda la ruta del archivo txt
ruta_txt = ".\total.txt"

#Resumen:
#   Variable que guarda una función lambda usada para multiplicar
multiplicacion = lambda number, porcentaje : number * porcentaje

#6
def carrito_de_compras(datos_insumos:list,marcas:dict):
    # Resumen:
    #     Función que crea una factura de compra en un diccionario. Donde cada producto es una key y sus value es el
    #     total del precio multiplicado la cantidad
    #     Tiene como parametro a la lista 'datos_insumos'
    #     Retorna un diccionario que funciona a modo de factura mostrando todos los productos y el total de cada uno
    respuesta = "Si"
    factura = {}
    bandera = False
    lista_productos = []
    
    
    print("MARCAS: ")
    for marca in marcas:
        print(f"    {marca}")
    
    while respuesta=="Si":
        while bandera == False:
            marcas_usuario = input("INGRESE EL NOMBRE DE LA MARCA: ")
            while marcas_usuario not in marcas:
                marcas_usuario = input("REINGRESE EL NOMBRE DE LA MARCA: ")
            for linea in datos_insumos:
                if re.search(marcas_usuario, linea[2]):
                    print(f"    Producto: {linea[1]}")
                    lista_productos.append(linea[1])
            producto = input("INGRESE EL NOMBRE DEL PRODUCTO: ")
            while producto not in lista_productos:
                producto = input("REINGRESE EL NOMBRE DEL PRODUCTO: ")
            lista_productos.clear()
            for linea in datos_insumos:
                if re.search(marcas_usuario, linea[1]):
                    bandera = True
                    cantidad = input(f"INGRESE LA CANTIDAD DEL PRODUCTO({linea[5]}): ")
                    while not cantidad.isdigit() or int(cantidad) > linea[5]:
                        cantidad = input(f"REINGRESE UNA CANTIDAD QUE SEA MENOR O IGUAL AL STOCK({linea[5]}): ")
                    cantidad = float(cantidad)
                    linea[5] = int(linea[5] - cantidad)
                    precio = float(linea[3].strip("$"))
                    key = linea[1]
                    factura[key] = multiplicacion(precio,cantidad)
        respuesta = input("¿DESEA SEGUIR INGRESANDO PRODUCTOS(Si/No)?: ")
        while respuesta != "Si" and respuesta != "No": 
            respuesta = input("REINGRESE UNA RESPUESTA CORRECTO(Si/No): ")
        if respuesta == "Si":
            bandera = False
    return factura

def total_compra(carro_compras:dict):
    # Resumen:
    #     Función que hace una suma total de todos los value de cada una de las keys de un diccionario
    #     Tiene como parametro al diccionario 'carro_compras'
    #     Retorna un entero que sería el resultado de la suma total de los value
    suma_total = 0
    for valor in carro_compras.values():
        suma_total  = suma_total + valor
    return suma_total

def porcentaje(total):
    # Resumen:
    #     Función que hace el subtotal de los precios de los productos
    #     Tiene como parametro a al str 'total'
    #     Retorna el resultado del impuesto, ingresado por el usuario, multiplicado por el total de los precios
    impuesto = input("INGRESE EL PORCENTAJE DEL IMPUESTO(Tiene que ser de entre 0% y 100%): ")
    while not impuesto.isdigit() or int(impuesto) < 0 or int(impuesto) > 100:
        impuesto = input("REINGRESE EL PORCENTAJE DEL IMPUESTO(Tiene que ser de entre 0% y 100%): ")
    impuesto = int(impuesto)
    impuesto = impuesto/100
    sub_total = total - multiplicacion(total,impuesto)
    sub_total = round(sub_total,3)
    return sub_total

def modificar_txt(ruta_txt:str,carro_compras:dict,total:float,sub_total:float):
    # Resumen:
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
    # Resumen:
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
    # Resumen:
    #     Función que abre el archivo json y escribe la información del diccionario de Disco Duro.
    #     Tiene como parametro a la ruta del archivo json donde se escribirán el diccionario.
    #     También tiene como parametro al diccionario donde están guardados los discos.
    with open(ruta_json,'w+', encoding='UTF-8') as file:
        json.dump(dict_disco,file,indent=4)

8#
def leer_archivo_json(ruta_json:str):
    # Resumen:
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
    # Resumen:
    #     Función que abre que abre una lista, y se fija si alguno de sus items contiene el signo '$'
    #     en caso de que lo tenga le hace un aumento del  del 8,4%.
    #     Tiene como parametro a una lista.
    #     Retorna un string compuesto del resultado del aumento concatenado con el signo '$'
    
    resultado = 0
    for item in lista:
        if isinstance(item, str) and re.search(r'\$', item):
            numero = float(item.strip("$"))
            resultado = numero + multiplicacion(numero,0.084)
            resultado = "$"+str(resultado)
    return resultado

def inflacion_lista(datos_insumos:list):
    # Resumen:
    #     Función que abre que crea una lista en la que los precios tienen un aumento del 8,4%
    #     Tiene como parametro a la lista 'datos_insumos'.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    for linea in datos_insumos:
        calculo = list((map(inflacion,[linea])))
        linea[3] = calculo[0]
    return datos_insumos


def reemplazar_csv(ruta:str,lista_inflacionaria:list):
    # Resumen:
    #     Función que abre sobreescribe el archivo csv de insumos con los precios actualizados a la inflación de m
    #     Tiene como parametro a la ruta del archivo json donde se ubican los discos.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    with open(ruta,'w+',encoding='UTF-8', newline="") as file:
        escritura = csv.writer(file)
        for linea in lista_inflacionaria:
            escritura.writerow(linea)

#11
def traer_marcas(ruta_marcas:str):
    # Resumen:
    #     Función que guarda cada una de las marcas existentes en el archivo de marcas.txt.
    #     Tiene como parametro a la ruta del archivo txt donde se ubican las marcas.
    #     Retorna una lista con las marcas del archivo txt como items.
    marcas = []
    with open(ruta_marcas,'r',encoding='UTF-8') as file:
        for linea in file:
            marcas.append(linea.strip("\n"))
    return marcas

def elegir_marca(listado_marcas:list):
    # Resumen:
    #     Función que permite al usuario elegir entre las marcas guardadas dentro del listado de marcas.
    #     Tiene como parametro a la lista donde están guardadas cada una de las marcas.
    #     Retorna una variable que contiene la marca elegida por el usuario.
    marca_elegida = ""
    bandera = False
    while bandera == False:
        eleccion = input("INGRESE EL NOMBRE DE LA MARCA DEL NUEVO PRODUCTO: ")
        for item in listado_marcas:
            if re.search(eleccion,item):
                marca_elegida = item
                bandera = True
    return marca_elegida


def crear_id(datos_insumos):
    # Resumen:
    #     Función que crea un id apartir de los existentes dentro de datos insumos.
    #     Tiene como parametro a la lista datos_insumos.
    #     Retorna una variable que contiene el id asignado.
    ids_existentes = len(datos_insumos)
    id = ids_existentes + 1
    return id
    
def ingresar_precio():
    # Resumen:
    #     Función que le permite al usuario asignarle un precio(entero o flotante), que luego el programa convierte a flotante, para luego pasarlo a str y agregarle el '$'.
    #     Retorna una variable que contiene el precio asignado por el usuario en modo de string con el símbolo '$'.
    precio = input("INGRESE EL PRECIO QUE QUIERA: ")
    while not precio.isdigit() or int(precio) <= 0:
        precio = input("REINGRESE UN PRECIO VÁLIDO: ")
    precio = float(precio)
    precio_final = "$"+ str(precio)
    return precio_final

def agregar_caracteristica():
    # Resumen:
    #     Función que le permite al usuario asignarle una o más características al insumo.
    #     Retorna una variable que la o las características que el usuario asignó.
    string_caracteristica = ""
    respuesta = "Si"
    caract_ingresada = input("INGRESE UNA CARACTERÍSTICA: ")
    string_caracteristica = string_caracteristica + caract_ingresada
    respuesta = input("DESEA AGREGAR MÁS CARACTERÍSTICAS(Si/No): ")
    while respuesta != "Si" and respuesta != "No": 
        respuesta = input("REINGRESE UNA RESPUESTA CORRECTA(SI/NO): ")
    while respuesta == "Si":
        caract_ingresada = input("INGRESE UNA CARACTERÍSTICA: ")
        string_caracteristica = string_caracteristica + "|!*|" + caract_ingresada
        respuesta = input("DESEA AGREGAR MÁS CARACTERÍSTICAS(Si/No): ")
    return string_caracteristica

def crear_linea(listado_marcas:list,datos_insumos:list):
    # Resumen:
    #     Función que apartir de las anteriores funciones crea una lista cuyos items son los mismos tipos de datos que tiene cada uno de los insumos preexistentes.
    #     Tiene como parametro al listado_de_marcas y a datos insumos.
    #     Retorna una lista cuyos items y datos están de esta manera "ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS". De la misma manera que el resto de los insumos.
    linea = []
    id_elegido = crear_id(datos_insumos)
    linea.append(id_elegido)

    novo_producto = input("INGRESE EL NOMBRE DEL NUEVO PRODUCTO: ")
    linea.append(novo_producto)
    for item in listado_marcas:
        print(f"{item}")

    marca_elegida = elegir_marca(listado_marcas)
    linea.append(marca_elegida)

    precio = ingresar_precio()
    linea.append(precio)

    caracteristica = agregar_caracteristica()
    linea.append(caracteristica)

    stock = random.randint(0,10)
    linea.append(stock)
    return linea

def elegir_archivo(ruta_arch_csv,ruta_arch_json,datos_insumos,diccionario_actualizado):
    # Resumen:
    #     Función que le permite al usuario elegir el tipo de archivo en el que guardar la lista de insumos actualizada con los productos que agregó el usuario. Las opciones serían json o csv.
    #     Tiene como parametro al diccionario_actualizado(para usarlo en json), datos insumos(para usarlo en csv) y ruta_arch_csv y, ruta_arch_json que las rutas de los archivos csv y json.
    elegir = input("INGRESE EL TIPO DE ARCHIVO(csv/json): ")
    while elegir != "csv" and elegir != "json":
        elegir = input("INGRESE UN TIPO DE ARCHIVO CORRECTO(csv/json): ")
    if elegir == "csv":
         with open(ruta_arch_csv,'w+',encoding='UTF-8', newline="") as file:
            escritura = csv.writer(file)
            for linea in datos_insumos:
                escritura.writerow(linea)
    else:
         with open(ruta_arch_json,'w+',encoding='UTF-8', newline="") as file:
            json.dump(diccionario_actualizado,file,indent=4)
    
    
                

    





