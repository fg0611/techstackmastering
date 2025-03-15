¡Claro! Aquí tienes ejemplos prácticos de cada uno de los conceptos mencionados en la sección de **Estructuras de Datos**:

---

### 1. **Listas**
Las listas son colecciones **ordenadas** y **mutables** (pueden modificarse).

#### Creación, acceso y modificación
```python
# Creación
mi_lista = [1, 2, 3, 4, 5]

# Acceso
print(mi_lista[0])  # Salida: 1 (primer elemento)
print(mi_lista[-1]) # Salida: 5 (último elemento)

# Modificación
mi_lista[0] = 10
print(mi_lista)  # Salida: [10, 2, 3, 4, 5]
```

#### Métodos comunes
```python
# append(): Añade un elemento al final
mi_lista.append(6)
print(mi_lista)  # Salida: [10, 2, 3, 4, 5, 6]

# extend(): Añade varios elementos
mi_lista.extend([7, 8])
print(mi_lista)  # Salida: [10, 2, 3, 4, 5, 6, 7, 8]

# insert(): Inserta un elemento en una posición específica
mi_lista.insert(1, 20)  # Inserta 20 en la posición 1
print(mi_lista)  # Salida: [10, 20, 2, 3, 4, 5, 6, 7, 8]

# remove(): Elimina la primera ocurrencia de un valor
mi_lista.remove(20)
print(mi_lista)  # Salida: [10, 2, 3, 4, 5, 6, 7, 8]

# pop(): Elimina y devuelve el elemento en una posición (por defecto, el último)
elemento = mi_lista.pop(1)  # Elimina el elemento en la posición 1
print(elemento)  # Salida: 2
print(mi_lista)  # Salida: [10, 3, 4, 5, 6, 7, 8]

# sort(): Ordena la lista
mi_lista.sort()
print(mi_lista)  # Salida: [3, 4, 5, 6, 7, 8, 10]

# reverse(): Invierte la lista
mi_lista.reverse()
print(mi_lista)  # Salida: [10, 8, 7, 6, 5, 4, 3]
```

#### Comprensión de listas
```python
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

### 2. **Tuplas**
Las tuplas son colecciones **ordenadas** e **inmutables** (no pueden modificarse).

#### Creación y uso
```python
# Creación
mi_tupla = (1, 2, 3, 4, 5)

# Acceso
print(mi_tupla[0])  # Salida: 1

# Intento de modificación (generará un error)
# mi_tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Uso para datos constantes
coordenadas = (40.7128, -74.0060)  # Latitud y longitud de Nueva York
print(coordenadas)
```

---

### 3. **Diccionarios**
Los diccionarios son colecciones de pares **clave-valor**.

#### Creación, acceso y modificación
```python
# Creación
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceso
print(mi_diccionario['nombre'])  # Salida: Juan

# Modificación
mi_diccionario['edad'] = 31
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

# Añadir nueva clave-valor
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
```

#### Métodos comunes
```python
# keys(): Obtener todas las claves
print(mi_diccionario.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])

# values(): Obtener todos los valores
print(mi_diccionario.values())  # Salida: dict_values(['Juan', 31, 'Madrid', 'Ingeniero'])

# items(): Obtener pares clave-valor
print(mi_diccionario.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 31), ('ciudad', 'Madrid'), ('profesion', 'Ingeniero')])

# get(): Obtener el valor de una clave (sin lanzar error si no existe)
print(mi_diccionario.get('pais', 'Desconocido'))  # Salida: Desconocido

# update(): Actualizar con otro diccionario
mi_diccionario.update({'pais': 'España', 'edad': 32})
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 32, 'ciudad': 'Madrid', 'profesion': 'Ingeniero', 'pais': 'España'}
```

---

### 4. **Conjuntos**
Los conjuntos son colecciones **no ordenadas** y **sin duplicados**.

#### Creación y operaciones básicas
```python
# Creación
mi_conjunto = {1, 2, 3, 4, 5}

# Añadir elementos
mi_conjunto.add(6)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar elementos
mi_conjunto.remove(3)
print(mi_conjunto)  # Salida: {1, 2, 4, 5, 6}

# No permite duplicados
mi_conjunto.add(2)
print(mi_conjunto)  # Salida: {1, 2, 4, 5, 6}
```

#### Operaciones entre conjuntos
```python
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión (|)
print(conjunto_a | conjunto_b)  # Salida: {1, 2, 3, 4, 5, 6}

# Intersección (&)
print(conjunto_a & conjunto_b)  # Salida: {3, 4}

# Diferencia (-)
print(conjunto_a - conjunto_b)  # Salida: {1, 2}
```

---

### Resumen
- **Listas**: Colecciones ordenadas y mutables.
- **Tuplas**: Colecciones ordenadas e inmutables.
- **Diccionarios**: Colecciones de pares clave-valor.
- **Conjuntos**: Colecciones no ordenadas y sin duplicados.