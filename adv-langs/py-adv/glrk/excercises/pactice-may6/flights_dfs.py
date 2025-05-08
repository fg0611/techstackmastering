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

def travel(flights: list, ori: str, dest: str, path: set, steps = 0):


    if ori == dest:
        return steps
    
    path.add(ori)
    min_flights = float('inf')
    
    for c_start, c_end in flights:
        if c_start == ori and c_end not in path:
            new_steps = travel(flights, c_end, dest, path.copy(), steps+1)
            if new_steps != -1:
                min_flights = min(min_flights, new_steps)
    
    return min_flights if min_flights != float('inf') else -1
    
            
conns = [["NYC", "CHI"], ["CHI", "SEA"], ["NYC", "ATL"], ["ATL", "DEN"], ["DEN", "SEA"], ["CHI", "DEN"]]
ori= "NYC"
dest= "SEA"

# conns= [["SFO", "LAX"], ["LAX", "DFW"], ["DFW", "JFK"], ["JFK", "BOS"], ["BOS", "MIA"]]
# ori= "SEA"
# dest= "MIA"

# conns= [["SFO", "LAX"], ["SEA","JFK"], ["LAX", "DFW"], ["DFW", "JFK"], ["JFK", "BOS"], ["BOS", "MIA"]]
# ori= "SEA"
# dest= "MIA"

print(travel(conns, ori, dest, set()))

# Salida: 2
# Explicación:
# Hay dos rutas posibles:

# NYC → CHI → SEA (2 vuelos)

# NYC → ATL → DEN → SEA (3 vuelos)
# El mínimo es 2 vuelos.

