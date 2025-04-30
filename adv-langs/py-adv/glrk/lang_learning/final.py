#  python 🐍

# print(2**(1/2))

lista = [1, 10.4, 2, 'a', [3, 2], 1.4, {'clave': 'valor'}]

# Filtrar solo números y strings
filtrados = [x for x in lista if isinstance(x, (int, float, str))]
lista_ordenada = sorted(filtrados, key=lambda x: (isinstance(x, str), str(x)))

print(lista_ordenada)  # Output: [1, 2, 'a']


# l1 = ['x', 1, 2, 4, 2**(1/2), 5, 10.47586, 'a']
# l2 = [1, 2, 4, 8, 6, 100, 'X']

# s = sorted(l1, key= lambda x: (isinstance(x, str), str(x)))
# s = sorted(l1, key= lambda x: str(x))

# print(s)

# print(ord('x'))
# print(ord('0'))
# l3 = ['a', '0']
# l3.sort()
# print(l3)

# n = [el for el in l1 if isinstance(el, (int, float))]
# t = [el for el in l1 if isinstance(el, str)]

# n.sort()
# t.sort()

# print(l1)

# print(n + t)



# print("union", l1 | l2) # union
# print("intersection", l1 & l2) # valores compartidos
# print("diferencia", l1 - l2) # valores de l1 que no estan en l2
# print("diferencia simetrica", l1 ^ l2) # valores que no comparten

# print(list(l1).sort())

# d = {"nombre": "fran", "edad": 30, "dni": 123123123, 'props': ['auto', 'casa'], 'familiares': ['ana', 'fran']}

# print(d.get('propiedades', "no existe"))

# d = {k: v for k, v in d.items() if isinstance(v, list) and 'ana' in v}

# print(d)

# t = (1, 2, 3, 4, 5, 5)

# t[0] = 0

# print(t)

# for k, v in d.items():
#     print(f'clave {k} valor {v}')

# for v in d.values():
#     print(v)

# d = {}

# l = [1, 2, 3]
# print(l)

# l.insert(len(l), 'fran')

# # l = [n for n in l if n != 3]
# print(l)

# l.pop()

# print(l)

# t = str({})

# print(t)

# print(isinstance(t, str))

# class Hogar:
#     pass

# class Casa(Hogar):
#     pass

# duplex = Casa()

# print(isinstance(duplex, Hogar))


# strings o texto
# TIPO
# INSTANCIA O CLASE
# OPERACIONES: SLICING, LISTAR, ELMINAR CONTENIDO, TRANSFORMAR, UNIR, SEPARAR,
# EDITAR, REEMPLAZAR, ORDENAR
# f string, IN

# texto = 'fran: hola como estas? y beto le dice: hola Fran todo bien!'


# dec = 'wkljehrk123.2'

# try:
#     print(float(dec))
# except Exception as e:
#     print(e)


# print(texto.replace('hola', ''))

# tl = list(texto)

# print(texto.split())

# print(' '.join([p for p in texto.split() if p != 'hola']))

# a p le agrego letras
# a medida que agregue letras voy verificando 'hola' in p
# si lo encuentra entonces estoy en el indice
# texto[i-3, i+1] = ''


# def mi_replace(texto, borrar, reemplazo):
#     t2 = ''
#     for l in texto:
#         t2 += l
#         if borrar in t2:
#             t2 = t2[0 : len(t2)-len(borrar)] + reemplazo
#     return t2

# print(texto)
# print(mi_replace(texto, 'beto', 'Ramon'))


# a = [1, 2, 3]
# b = a
# c = b

# d = b

# print(c is b)

# d.append(4)

# print(d)
# print(a)

# print(list(texto))

# print(enumerate(texto))

# for i, l in enumerate(texto):
#     print(f'en el indice {i} va el char {l}')



# print(texto[:-1] + ' fran?')

# print(texto*2)

# print('.' in texto)

# print(isinstance(texto, str))

# print(range(0, len(texto)-1))
# print()


# r = range(0, 5)
# s = 'hola'

# print(s.replace('a', ''))
# print(s[:-1])

# print(s[0:4])

# for i in range(0, len(texto)):
#     print(f'en el indice {i} va el char {texto[i]}')


