#  python 🐍

sistema_archivos = {
    "raiz": {
        "documentos": {
            "informe.txt": {"tamaño": "10KB", "tipo": "texto", "metadata": [1, 2, 3]},
            "presentacion.pptx": {"tamaño": "2MB", "tipo": "presentacion"}
        },
        "imagenes": {
            "foto1.jpg": {"tamaño": "500KB", "tipo": "imagen"},
            "logo.png": {"tamaño": "100KB", "tipo": "imagen"}
        },
        "usuario.dat": {"tamaño": "5KB", "tipo": "binario"}
    }
}

# hacer un prints para ver toda la estructura

# recorre los dicts y si en su k,v la v es otro dict entonces volver a ejec
# sino simplemente imprime k,v
# caso base
def pest(d, lvl):
     if isinstance(d, dict):
          for k, v in d.items():
               if not isinstance(v, dict):
                    print(f'{lvl * "-"} {lvl} - {k} {v}')
               else:
                    print(f'{lvl * "-"} {lvl} - {k}')
                    pest(v, lvl+1)

pest(sistema_archivos, 0)

# print(sistema_archivos['raiz'].items())

# l = [10, 2, 35, 3, 3, 4, 5, 5, 10]

# l = sorted(list(set(l)))

# print(l)

# print(l[::-1])



# agrupacion por informacion dentro de un diccionario
# personas = [ # agrupar por cuidad en un diccionario
#     {"nombre": "Ana", "ciudad": "Córdoba"},
#     {"nombre": "Beto", "ciudad": "Buenos Aires"},
#     {"nombre": "Carlos", "ciudad": "Córdoba"},
#     {"nombre": "Diana", "ciudad": "Mendoza"}
# ]

# recorrer la lista
# leer el valor de la key ciudad o crearla y asigarle una lista vacia
# insertar el dato nombre 
# personas_por_ciudad = {}
# for d in personas:
#     c = d['ciudad'] 
#     personas_por_ciudad[c] = personas_por_ciudad.get(c, []) + [d['nombre']]
# print(personas_por_ciudad)

# contar apariciones en listas o diccionarios usando diccionarios
# nums = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6]
# c = {}
# for n in nums:
#     c[n] = c.get(n, 0) + 1
# print(c)

# d = {"nombre": "Ana", "edad": 30, "ciudad": "Córdoba"}
# d1 = {"ciudad": "Córdoba"}

# d2 = {**d, **d1} # combinacion de diccionarios

# print(d2)

# print(type(d1.keys()))

# print(list(d1.keys()))

# print(d)

# dict name: n_letters
# nombres = ["Ana", "Beto", "Carlos"]

# r = { n : len(n) for n in nombres }

# print(r)

