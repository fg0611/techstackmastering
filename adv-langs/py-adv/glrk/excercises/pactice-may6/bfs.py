grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

inicio = 'A'
objetivo = 'G'

from collections import deque

def bfs(data, inicio, fin):

    cola = deque([(inicio, [inicio])])
    vistos = {inicio}

    while cola:
        nodo_actual, camino = cola.popleft()

        if nodo_actual == fin: # caso base
            return camino
        
        for vecino in data.get(nodo_actual, []):
            if vecino not in vistos:
                vistos.add(vecino)
                cola.append((vecino, [*camino, vecino]))
    return None

busqueda = bfs(grafo, inicio, objetivo)

print(busqueda)