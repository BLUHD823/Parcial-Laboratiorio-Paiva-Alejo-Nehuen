from funciones_ordenamiento import *
from funciones_archivos import *
#Resumen:
#   Variables que guardan las rutas del archivos json donde se guardan los discos duros y la ruta del archivo .csv con los insumos
ruta_json ="./discos.json"
ruta = "./Insumos.csv - Hoja 1.csv"
ruta_txt = "./total.txt"
ruta_marcas = "./marcas.txt"
ruta_arch_csv = "./archivo.csv"
ruta_arch_json = "./archivo.json"

def menu(ruta,ruta_json):
    try:
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
            print("11-CREAR NUEVO PRODUCTO. ")
        
            eleccion = input("INGRESE SU RESPUESTA: ")
            while not  eleccion.isdigit() or int(eleccion) <=0 or int(eleccion) >11: 
                eleccion = input("REINGRESE SU RESPUESTA CON LOS VALORES ADECUADOS: ")
            eleccion = int(eleccion)
            match eleccion:
                case 1:
                    listado = leer_csv(ruta)
                    datos_insumos = listar_lineas(listado)
                    agregar_elemento(datos_insumos)
                    for linea in datos_insumos:
                        print(linea)
                case 2:
                    diccionario_marcas = lista_cantidad_marca(datos_insumos)
                    for key, value in diccionario_marcas.items(): 
                        print(f"{key}:{value}")
                case 3: 
                    diccionario_marcas = lista_cantidad_marca(datos_insumos)
                    listar_insumos_marca(diccionario_marcas,datos_insumos)
                case 4: 
                    listar_insumos_caracteristica(datos_insumos)
                case 5:
                    diccionario = crear_diccionario(datos_insumos)
                    diccionario_ordenado_descendente = ordenar_diccionario_asc_des(diccionario,'Precio', True)
                    for linea in diccionario_ordenado_descendente:
                        for key,value in linea.items():
                            print(f"{key}: {value}")
                        print("\n")
                    print("///////////////////////////////////////////////////////////////////////////////////////////")
                    diccionario_ordenado_alfabeticamente = ordenar_diccionario_asc_des(diccionario_ordenado_descendente,'Marca', False)
                    for linea in diccionario_ordenado_alfabeticamente:
                        for key,value in linea.items():
                            print(f"{key}: {value}")
                        print("\n")
                case 6:
                        diccionario_marcas = lista_cantidad_marca(datos_insumos)
                        carro_compras = carrito_de_compras(datos_insumos,diccionario_marcas)
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
                case 10:
                    print("SALIENDO DEL PROGRAMA...")
                    return
                case 11:
                    listado_marcas = traer_marcas(ruta_marcas)
                    lista = crear_linea(listado_marcas,datos_insumos)
                    print(lista)
                    datos_insumos.append(lista)
                    diccionario_actualizado =  crear_diccionario(datos_insumos)
                    elegir_archivo(ruta_arch_csv,ruta_arch_json,datos_insumos,diccionario_actualizado)
    except UnboundLocalError:
         print("    TIENES QUE INICIALIZAR LA PRIMERA FUNCIÓN.")
         menu(ruta,ruta_json)
menu(ruta,ruta_json)


