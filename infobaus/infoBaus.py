from funciones_ordenamiento import *
from funciones_archivos import *

ruta_json ="C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\discos.json"
ruta_txt = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\total.txt"
ruta = "C:\\Users\\Alejo\\Desktop\\bauss\\Parcial-Laboratiorio\\infobaus\\Insumos.csv - Hoja 1.csv"

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
        while eleccion <=0 or eleccion >10:
            eleccion = int(input("REINGRESE SU RESPUESTA CON LOS VALORES ADECUADOS: "))
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

try:
    menu()
except UnboundLocalError:
    print("\nPARA USAR EL RESTO DE LAS FUNCIONES, PRIMERO TIENE QUE INICIALIZAR LAS PRIMERAS DOS OPCIONES '1-TRAER DATOS DESDE ARCHIVO.' Y '-2LISTAR CANTIDAD POR MARCA.' ")
    menu()

