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

def imprimir_nombres():
    # La función imprimir_materias verifica si la entrada es un diccionario o una lista.
    # Si es un diccionario, itera sobre las claves y los valores.
    # Si la clave es "nombre" y el valor es una cadena, imprime el valor.
    # En cualquier otro caso, llama a imprimir_materias con el valor como entrada.
    # Si la entrada es una lista, itera sobre los elementos y llama a imprimir_materias 
    # con cada elemento como entrada.
    print()
    
