#  python 🐍 - tuplas
tupla = (1, 1, 1, 1, 2, 3, 4, 2)
# print(tupla.count(2))
# print(tupla[::-1])
# nset = set(tupla)
# print(nset)
# d = {1:2, 2:3}

a = {1, 2, 3, 4}
b = {8, 1, 3}

print(a | b) # union() - los une dejan duplicados fuera
print(a & b) # intersection() - elementos comunes entre ambos 
print(a-b) # difference() - elementos que del 1ero que no estan en el 2do
print(a^b) # symmetric_difference() - elementos que no comparten




# print(d)
# print({v:k for k,v in d.items()})
# print(set(d))

# print(len(tupla))

# print(isinstance(tupla, tuple))
# print(isinstance('tupla', (dict, str)))

# a, *b = tupla

# print(a) # primer dato
# print(b) # una lista con el resto de datos dentro de la tupla

# a, b, c, d = tupla



# s={1, 2, 3}
# print(type(s))
# print(isinstance(s, set))
