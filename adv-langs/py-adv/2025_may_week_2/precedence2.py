def findWord(arr):
    # split arr into pairs
    subs = [e.split('>') for e in arr]
    starts = {}
    ends = {}
    result = [] 
    for pair in subs:
        start, end = pair
        starts.setdefault(start, []).append(pair)
        ends.setdefault(end, []).append(pair)
    
    while subs:
        # iniciamos el flag de conexion encontrada
        found = False
        # comenzamos con el primer par y lo sacamos de subs
        if not result:
            result.append(subs.pop(0))
            found = True
        # ahora aislamos el 1er char y el ultimo de result
        r_start = result[0][0]
        r_end = result[-1][1]
        # insercion al inicio - buscamos R_START en el dict de ENDS
        if r_start in ends:
            conn_start_ends = [el for el in ends[r_start] if el in subs]
            if conn_start_ends:
                attach_to_beggining = conn_start_ends[0]
                result.insert(0,attach_to_beggining)
                subs.remove(attach_to_beggining)
                found = True
        # insercion al final - buscamos R_END en el dict de STARTS
        if not found and r_end in starts:
            conn_end_starts = [el for el in starts[r_end] if el in subs]
            if conn_end_starts:
                attach_to_ending = conn_end_starts[0]
                result.append(attach_to_ending)
                subs.remove(attach_to_ending)
                found = True
        # si no se encontro nada vaciar result, meter el primero en subs y remover la muestra de subs
        if subs and not found: 
            result = []
            result.append(subs.pop(0))
    
    return result
        
r = findWord(["I>N", "A>I", "P>A", "S>P"]) 
# sp pa ai in
print(r)

r2 = findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])
print(r2)
# po or rt tu ug ga al
# findWord(["P>E", "E>R", "R>U"])

# findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) // HUNGARY
# findWord(["I>F", "W>I", "S>W", "F>T"]) // SWIFT
r3 = findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])
print(r3)