import csv
import json
#Resumen:
#   Variable que guarda la ruta del archivo txt
ruta_txt = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\total.txt"

#Resumen:
#   Variable que guarda una función lambda usada para multiplicar
multiplicacion = lambda number, porcentaje : number * porcentaje

#6
def carrito_de_compras(datos_insumos:list):
    # Resumen:
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
                    key = linea[1]
                    factura[key] = multiplicacion(precio,cantidad)
        respuesta = input("¿DESEA SEGUIR INGRESANDO PRODUCTOS(Si/No)?: ")
        while respuesta != "Si" and respuesta != "No": 
            respuesta = input("REINGRESE UNA RESPUESTA CORRECTO(SI/NO): ")
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
    impuesto = int(input("INGRESE EL PORCENTAJE DEL IMPUESTO: "))
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
    if "$" in lista:
        numero = float(lista.strip("$"))
        resultado = numero + multiplicacion(numero,0.084)
        resultado = "$"+str(resultado)
    return resultado

def inflacion_lista(datos_insumos:list):
    # Resumen:
    #     Función que abre que crea una lista en la que los precios tienen un aumento del 8,4%
    #     Tiene como parametro a la lista 'datos_insumos'.
    #     Retorna una lista con los Discos Duros del archivo json como items.
    for linea in datos_insumos:
        calculo = list((map(inflacion,linea)))
        linea[3] = calculo[3]
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