En Python, los diccionarios son estructuras de datos que almacenan pares clave-valor. Aquí te explico cómo puedes ver y trabajar con estas claves y valores:

**1. Acceder a valores por clave:**

* La forma más directa de ver un valor es accediendo a él mediante su clave correspondiente:

```python
diccionario = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print(diccionario["nombre"])  # Salida: Ana
print(diccionario["edad"])    # Salida: 30
```

* Es importante tener en cuenta que si intentas acceder a una clave que no existe, Python generará un error `KeyError`. Para evitar esto, puedes usar el método `get()`.

**2. El método `get()`:**

* El método `get()` devuelve el valor asociado a una clave. Si la clave no existe, devuelve `None` (o un valor predeterminado que puedes especificar).

```python
diccionario = {"nombre": "Ana", "edad": 30}
print(diccionario.get("ciudad"))       # Salida: None
print(diccionario.get("ciudad", "Desconocida")) # Salida: Desconocida
```

**3. Iterar sobre claves y valores:**

* Puedes recorrer las claves y valores de un diccionario utilizando un bucle `for` junto con los métodos `keys()`, `values()` e `items()`:
    * `keys()`: Devuelve una vista de todas las claves del diccionario.
    * `values()`: Devuelve una vista de todos los valores del diccionario.
    * `items()`: Devuelve una vista de todos los pares clave-valor como tuplas.

```python
diccionario = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# Iterar sobre las claves
for clave in diccionario.keys():
    print(clave)

# Iterar sobre los valores
for valor in diccionario.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
```

**4. Comprobar la existencia de una clave:**

* Puedes usar el operador `in` para verificar si una clave existe en un diccionario:

```python
diccionario = {"nombre": "Ana", "edad": 30}
if "nombre" in diccionario:
    print("La clave 'nombre' existe.")
```

**Resumen de métodos útiles:**

* `diccionario.keys()`: Obtener todas las claves.
* `diccionario.values()`: Obtener todos los valores.
* `diccionario.items()`: Obtener todos los pares clave-valor.
* `diccionario.get(clave)`: Obtener el valor de una clave (sin errores).
* `clave in diccionario`: Comprobar si una clave existe.

Con estos métodos y técnicas, puedes acceder, manipular y recorrer de manera efectiva los pares clave-valor en tus diccionarios de Python.
