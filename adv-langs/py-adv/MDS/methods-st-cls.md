En Python, los **métodos estáticos** y los **métodos de clase** son dos tipos de métodos especiales que se definen dentro de una clase, pero tienen comportamientos y usos diferentes. Ambos se definen usando decoradores (`@staticmethod` y `@classmethod`), y su principal diferencia radica en cómo interactúan con la clase y sus instancias.

---

### 1. **Métodos Estáticos (`@staticmethod`)**
Un método estático es un método que **no recibe implícitamente** ni la instancia (`self`) ni la clase (`cls`) como primer argumento. Es como una función normal, pero pertenece al espacio de nombres de la clase.

#### Características:
- No accede ni a la instancia (`self`) ni a la clase (`cls`).
- Se usa para tareas que no dependen del estado de la clase o de la instancia.
- Se define con el decorador `@staticmethod`.

#### Ejemplo:
```python
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

# Uso
resultado = Matematica.sumar(5, 10)
print(resultado)  # Salida: 15
```

#### ¿Cuándo usar `@staticmethod`?
- Cuando la funcionalidad no necesita acceder a atributos de la clase o de la instancia.
- Para organizar funciones relacionadas con la clase, pero que no dependen de su estado.

---

### 2. **Métodos de Clase (`@classmethod`)**
Un método de clase recibe la **clase** (`cls`) como primer argumento en lugar de la instancia (`self`). Esto permite acceder a los atributos y métodos de la clase.

#### Características:
- Recibe la clase (`cls`) como primer argumento.
- Puede acceder y modificar atributos de la clase.
- Se usa comúnmente para crear "constructores alternativos".
- Se define con el decorador `@classmethod`.

#### Ejemplo:
```python
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_string(cls, cadena):
        dia, mes, año = map(int, cadena.split('-'))
        return cls(dia, mes, año)  # Crea una nueva instancia de Fecha

# Uso
fecha = Fecha.desde_string("25-12-2023")
print(fecha.dia, fecha.mes, fecha.año)  # Salida: 25 12 2023
```

#### ¿Cuándo usar `@classmethod`?
- Cuando necesitas crear instancias de la clase de manera alternativa (por ejemplo, desde un formato de cadena, archivo, etc.).
- Cuando necesitas acceder o modificar atributos de la clase.

---

### 3. **Diferencias Clave**

| Característica          | Método Estático (`@staticmethod`) | Método de Clase (`@classmethod`) |
|-------------------------|-----------------------------------|----------------------------------|
| **Primer argumento**    | No recibe `self` ni `cls`.        | Recibe `cls` (la clase).         |
| **Acceso a la clase**   | No puede acceder a la clase.      | Puede acceder a la clase.        |
| **Acceso a la instancia** | No puede acceder a la instancia. | No puede acceder a la instancia directamente. |
| **Uso común**           | Funciones utilitarias.            | Constructores alternativos o manipulación de la clase. |

---

### 4. **¿Por qué se usan los decoradores `@staticmethod` y `@classmethod`?**
Los decoradores `@staticmethod` y `@classmethod` se usan para modificar el comportamiento de los métodos dentro de una clase:
- **`@staticmethod`**: Le dice a Python que el método no necesita acceso a la instancia (`self`) ni a la clase (`cls`). Es simplemente una función asociada a la clase.
- **`@classmethod`**: Le dice a Python que el método debe recibir la clase (`cls`) como primer argumento, permitiendo acceder a los atributos y métodos de la clase.

---

### 5. **Ejemplo Combinado**
```python
class Herramientas:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

    @classmethod
    def crear_herramienta(cls, nombre):
        herramienta = cls()  # Crea una instancia de la clase
        herramienta.nombre = nombre
        return herramienta

# Uso de métodos estáticos
print(Herramientas.es_par(10))  # Salida: True

# Uso de métodos de clase
herramienta = Herramientas.crear_herramienta("Martillo")
print(herramienta.nombre)  # Salida: Martillo
```

---

### Resumen
- **Método estático (`@staticmethod`)**: No recibe `self` ni `cls`. Es como una función normal dentro de una clase.
- **Método de clase (`@classmethod`)**: Recibe `cls` como primer argumento. Útil para constructores alternativos o manipulación de la clase.
- **Decoradores**: `@staticmethod` y `@classmethod` modifican el comportamiento de los métodos para indicar cómo deben interactuar con la clase y sus instancias.

¡Espero que esta explicación te haya sido útil! 😊