lista = [1,5,2,3,6,8,34,7]



def ordenar_mayor(numeros:list):
    tam = len(numeros)
    for i in range(0, tam - 1):
        for j in range(i + 1, tam):
            if numeros[i] > numeros[j]:
                aux = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = aux
    return numeros

print(lista)
print(ordenar_mayor(lista))


lista_letras = ["a","g","f","t","b"]

def ordenar_alf(letras:list):
    tam = len(letras)
    for i in range(0, tam - 1):
        for j in range(i + 1, tam):
            if letras[i] > letras[j]:
                aux = letras[i]
                letras[i] = letras[j]
                letras[j] = aux
    return letras

print(ordenar_alf(lista_letras))
