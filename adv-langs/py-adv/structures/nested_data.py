datos_estudiantes = {
    "estudiantes": [
        {
            "nombre": "Ana García",
            "edad": 20,
            "materias": [
                {"nombre": "Matemáticas", "calificaciones": [85, 90, 92]},
                {"nombre": "Historia", "calificaciones": [78, 82, 80]},
            ],
        },
        {
            "nombre": "Carlos Pérez",
            "edad": 22,
            "materias": [
                {"nombre": "Programación", "calificaciones": [95, 98, 96]},
                {"nombre": "Física", "calificaciones": [88, 92, 90]},
            ],
        },
    ],
}

est = ""

# Acceder al nombre del primer estudiante
if datos_estudiantes.keys():
    est = datos_estudiantes[list(datos_estudiantes.keys())[0]]

if len(est) > 0:
    print(est[0].get("nombre"))

# Acceder a la calificación de la segunda materia del segundo estudiante
mk = "materias"
ck = "calificaciones"
nk = "nombre"
if len(est) > 1 and len(est[1].get("materias")) > 1:
    print(est[1][mk][1][ck])

# Iterar sobre las materias del primer estudiante
for m in range(0, len(est[0].get(mk, []))):
    print(est[0].get(mk)[m])

# Calcular el promedio de calificaciones de la primera materia del segundo estudiante
try:
    print("ejecutando")
    data = est[1].get(mk)[0].get(ck)
    print(data)
    print(sum(data) / len(data))
except Exception as e:
    print(e)

import statistics

try:
    print(statistics.mean(data))
except Exception as e:
    print(e)

# Agregar una nueva calificación a la primera materia del primer estudiante
try:
    print("agregar calif. al 1er est en su 1era materia")
    print(est[0].get(mk, [])[0].get(ck))
    est[0].get(mk, [])[0].get(ck).append(95)
    print(est[0].get(mk, [])[0].get(ck))
except Exception as e:
    print(e)

# Agregar una nueva materia al segundo estudiante
try:
    print("Agregar una nueva materia al segundo estudiante")
    materia = {nk: "Plastilina I", ck: [60, 80, 100]}
    est[1].get(mk).append(materia)
    print(est[1])
except Exception as e:
    print(e)


# funcion para obt promedio de todas las materias de un estudiante o de una materia
def obtener_promedio(nombre, materia):
    if not isinstance(nombre, str):
        raise Exception("el nombre es obligatorio")
    if materia and not isinstance(materia, str):
        raise Exception("la materia debe ser un string")

    estudiante = {}
    for e in est:
        if nombre.lower() in e.get(nk, "").lower():
            estudiante = e
            break

    print("____________________________")
    print("________ ENCONTRADO ________")
    print(estudiante)
    if nombre and materia:
        promedio = -1
        for m in estudiante.get(mk, []):
            if m.get(nk, "").lower() == materia.lower():
                promedio = sum(m[ck]) / len(m[ck])
                break
        if promedio != -1:
            print(f"El promedio de {nombre} en {materia} es {promedio}")
    elif nombre:
        print(f'los promedis de {nombre} son:')
        for m in estudiante.get(mk, {}):
            prom = round(sum(m.get(ck, 0))/len(m.get(ck, 1)), 1)
            print(f"en {m.get(nk, '')} {prom}")
            
obtener_promedio("carlos", "")


# Escribe una función que encuentre al estudiante con el promedio general más alto.
# Escribe una función que agregue un nuevo estudiante a la estructura de datos.
# Escribe una función que encuentre la materia con el promedio más alto en todos los estudiantes.

# buscar keys y valores si existen
