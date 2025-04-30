lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzana", "banana", "cereza"]
lista3 = [True, False, True]
lista4 = [1, "hola", 3.14, True, [5, 6]]  # Lista con diferentes tipos de datos (anidada)
lista5 = [5, 2, 8, 1, 9, 3]
lista6 = ["z", "a", "m", "b"]
lista7 = [1, 2, 2, 3, 4, 2, 5]
lista8 = []  # Lista vacía

# metodos para ordenar y revertir listas
# sort (puede usar reverse=True) -> es inplace
# lista7.sort(reverse=True)
# print(lista7)
sorted(lista7)
print(lista7)

# metodos de buscar y contar elementos
# index(valor) -> puede lanzar error
# count(valor) 

# print(lista5.count(80))

# metodos de remocion: remove -> elim 1era ocurrencia,
#  pop -> elimina por indice y lo retorna y sin indice esp saca el ultimo 
# , del list[idx], clear -> vacia la lista

# metodos de modificacion: append, insert, extend
# lista5.insert(0, 1)
# print(lista5)
# lista2.extend(lista1)
# print(lista2)



# slicing de listas
# print(lista4[-1][0])
# invertir una lista
# print(lista1[::-1])


# reverse() -> invierte pero mod la lista y reversed() devuelve un iterador
# print(list(reversed(lista1)))
# lista1.reverse()
# print(lista1)




