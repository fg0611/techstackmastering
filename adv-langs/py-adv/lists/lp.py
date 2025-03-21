# numeros = [10, 20, 30, 40, 50]

# # Recorrer con un for
# for num in numeros:
#     print(num)

# # Recorrer con índice
# for i in range(len(numeros)):
#     print(f"Índice {i}: {numeros[i]}")

# nombres = ['a', 'b', 'c']
# l = len(nombres)
# i = 0
# while i < l:
#     print(nombres[i])
#     i+=1

# Crea un diccionario con tres claves (producto, precio, stock) y recórrelo.
# Muestra solo los valores con .values().


# l = list(range(10))
# print(l)

# print(l[::-1])

# print(l[::2])

d = {'producto': 'manzanas', 'precio': 2.5, 'stock': 100}
for v in enumerate(d.items()):
    print(f'{v}')