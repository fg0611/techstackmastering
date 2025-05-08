# Problema: Optimizador de Conexiones de Vuelo
# Descripción:
# Estás construyendo un optimizador de conexiones de vuelo para una aerolínea. La compañía opera en varias ciudades, y 
# los pasajeros a menudo necesitan tomar vuelos de conexión para llegar a sus destinos. Tu tarea es diseñar un algoritmo 
# que encuentre el número mínimo de conexiones de vuelo necesarias para que un pasajero viaje desde una ciudad de origen a una 
# ciudad de destino.
# Representación:
# La red de vuelos se representa como un grafo dirigido donde:
# Las ciudades son nodos
# Los vuelos directos son aristas
# Entrada:
# Un array de conexiones de vuelo (pares [origen, destino])
# Una ciudad de origen
# Una ciudad de destino
# Salida:
# El número mínimo de vuelos necesarios para viajar desde el origen al destino
# Si es imposible llegar al destino desde el origen, devolver -1

# Conexiones: [["SFO", "LAX"], ["LAX", "DFW"], ["DFW", "JFK"], ["JFK", "BOS"], ["BOS", "MIA"]]
# Origen: "SEA"
# Destino: "MIA"
# No hay ruta desde SEA a MIA en la red de vuelos dada

def travel(flights: list, ori, dest, paths: dict):

    less_flights = flights.copy()

    if len(flights):
        for el in flights:
            if el[0] == ori and tuple(el) not in paths:
                paths.setdefault(tuple(el), el)
            else:
                for k, v in paths.items():
                    if v[-1] == el[0]:
                        paths[k].extend(el)
            less_flights.remove(el)
            return travel(less_flights, ori, dest, paths)        
    else:
        if paths:
            counts = min([len(el)/2 for el in paths.values() if len(el)])
            return counts if counts else -1
        return -1          

    

        
# conns = [["NYC", "CHI"], ["CHI", "SEA"], ["NYC", "ATL"], ["ATL", "DEN"], ["DEN", "SEA"], ["CHI", "DEN"]]
# ori= "NYC"
# dest= "SEA"

# conns= [["SFO", "LAX"], ["LAX", "DFW"], ["DFW", "JFK"], ["JFK", "BOS"], ["BOS", "MIA"]]
# ori= "SEA"
# dest= "MIA"

conns= [["SFO", "LAX"], ["SEA","JFK"], ["LAX", "DFW"], ["DFW", "JFK"], ["JFK", "BOS"], ["BOS", "MIA"]]
ori= "SEA"
dest= "MIA"

print(travel(conns, ori, dest, {}))

# Salida: 2
# Explicación:
# Hay dos rutas posibles:

# NYC → CHI → SEA (2 vuelos)

# NYC → ATL → DEN → SEA (3 vuelos)
# El mínimo es 2 vuelos.

