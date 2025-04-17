def sum1n(n):
    # caso base
    if n == 1:
        return 1
    # caso recursivo
    return n + sum1n(n - 1)


# print(sum1n(5))


# encontrar el mayor valor de una lista
def higher(nlist):
    if not isinstance(nlist, list) or not nlist:
        return "must be list with at least 1 number"
    if len(nlist) == 1:
        return nlist[0]
    if nlist[0] > higher(nlist[1:]):
        # print(nlist[0])
        return nlist[0]
    else:
        return higher(nlist[1:])


l = [3, 7, 5, 2, 3, 2]
# l = [1]
# print(higher(l))

lista_anidada = [1, [2, 3], 4, [5, [6, 7]]]

# aplanar una lista.
#  base = si un elemento no es una lista se agrega al resultado
# recursivo = si un elemento es una lista se recorre


def aplanar_lista(data):
    if not isinstance(data, list) or not data:
        return "no es una lista con datos"
    result = []
    for e in data:
        if not isinstance(e, list):
            result.append(e)
        else:
            result.extend(aplanar_lista(e))
    return result


# print(aplanar_lista(lista_anidada))


# invertir una cadena de texto
# base = len 0 o 1
# recursivo = tomar el ult y concat con el resto de la cadena
def invertir(data):
    if len(data) > 1:
        return data[-1] + invertir(data[:-1])
    return data


# print(invertir('hola'))

categorias = {
    "nombre": "Electrónica",
    "subcategorias": [
        {
            "nombre": "Computadoras",
            "subcategorias": [
                {"nombre": "Laptops", "subcategorias": []},
                {"nombre": "PCs de escritorio", "subcategorias": []},
            ],
        },
        {
            "nombre": "Teléfonos",
            "subcategorias": [
                {"nombre": "Smartphones", "subcategorias": []},
                {"nombre": "Teléfonos fijos", "subcategorias": []},
                {
                    "nombre": "Otros",
                    "subcategorias": [{"nombre": "Laptops", "subcategorias": []}],
                },
            ],
        },
    ],
}
# Crear una función recursiva que imprima todos los nombres,
# con una indentación que muestre la jerarquía.

# def nombres_indentados(data, indent):
#     if data.get('nombre'):
#         print(f"{indent} {data['nombre']}")
#     if data.get('subcategorias'):
#         for e in data['subcategorias']:
#             nombres_indentados(e, f' {indent}')

# nombres_indentados(categorias, '*')


def nombres_indentados(data, nivel):
    if data.get("nombre"):
        print(f"{' ' * nivel} - {data['nombre']}")
    if data.get("subcategorias"):
        for e in data["subcategorias"]:
            nombres_indentados(e, nivel + 1)


# nombres_indentados(categorias, 1)


# Buscar un nodo por nombre y su nivel
def encontrar_categoria(data, nombre, nivel):
    if data.get("nombre") and data["nombre"].lower() == nombre.lower():
        print(f"{nombre} existe en {nivel}")
    if data.get("subcategorias"):
        for e in data["subcategorias"]:
            encontrar_categoria(e, nombre, nivel + 1)


# encontrar_categoria(categorias, "Laptops", 1)

diccionario_anidado = {"a": 1, "b": {"c": 2, "d": [3, 4]}, "e": [5, {"f": 6}]}

def aplanar_dic(data):  # res = lista de valores
    result = []
    if not isinstance(data, (dict, list)):
        result.append(data)
    elif isinstance(data, list):
        for e in data:
            result.extend(aplanar_dic(e))
    elif isinstance(data, dict):
        for val in data.values():
            result.extend(aplanar_dic(val))
    return result

# print(aplanar_dic(diccionario_anidado))

# version con comprension de listas
def aplanar_dic_comp(data):
    if not isinstance(data, (dict, list)):
        return [data]
    return [el for sub_el in (data if isinstance(data, list) else data.values()) for el in aplanar_dic_comp(sub_el)]

# print(aplanar_dic_comp(diccionario_anidado))

def aplanar_lista_comp(data):
    res = []
    for x in data:
        if not isinstance(data, list):
            res.append(data)
        else:
            res.extend(aplanar_dic_comp(x))
    return res

# print(aplanar_lista_1nivel([[4, 5], [7, 8]]))
print(aplanar_lista_comp([1, 2, 3, [4, 5], 6, [7, 8, 9]]))

lista_palabras = ["hola", "mundo", "python"]

def obtener_vocales(palabras):
    return [letra for palabra in palabras for letra in palabra if letra in 'aeiou']
    # result = []
    # for palabra in palabras:
    #     for letra in palabra:
    #         if letra in 'aeiou':
    #             result.append(letra)
    # return result

# print(obtener_vocales(lista_palabras))
