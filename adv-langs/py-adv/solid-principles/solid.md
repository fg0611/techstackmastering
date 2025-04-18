**SOLID** es un conjunto de **5 principios de diseño de software** que ayudan a crear código más limpio, mantenible y escalable. Fue acuñado por Robert C. Martin ("Uncle Bob") y se aplica especialmente en **programación orientada a objetos (POO)**.  

---

### 📌 **Los 5 principios SOLID** (con ejemplos sencillos en Python/Java/TypeScript):

#### **1. S - Principio de Responsabilidad Única (SRP)**  
> *"Una clase debe tener una sola razón para cambiar"* (es decir, una sola responsabilidad).  

**Ejemplo malo**:  
```python
class Usuario:
    def guardar_usuario(self):  # Responsabilidad: Persistencia
        pass
    def enviar_email(self):     # Responsabilidad: Notificación
        pass
```
**Ejemplo correcto**:  
```python
class Usuario:
    def guardar_usuario(self):
        pass

class EmailService:
    def enviar_email(self):
        pass
```

---

#### **2. O - Principio de Abierto/Cerrado (OCP)**  
> *"Las clases deben estar abiertas para extensión pero cerradas para modificación"*.  

**Ejemplo malo**:  
```python
class Calculadora:
    def calcular(self, tipo, a, b):
        if tipo == "suma":
            return a + b
        elif tipo == "resta":  # Requiere modificar la clase para añadir operaciones
            return a - b
```
**Ejemplo correcto**:  
```python
class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

# Extiende sin modificar la clase Calculadora
class Calculadora:
    def calcular(self, operacion, a, b):
        return operacion.calcular(a, b)
```

---

#### **3. L - Principio de Sustitución de Liskov (LSP)**  
> *"Las clases derivadas deben poder sustituir a sus clases base sin alterar el comportamiento"*.  

**Ejemplo malo**:  
```python
class Pajaro:
    def volar(self):
        pass

class Pinguino(Pajaro):  # ¡Los pingüinos no vuelan!
    def volar(self):
        raise Exception("No puedo volar")  # Viola LSP
```
**Ejemplo correcto**:  
```python
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        pass

class Pinguino(Ave):  # No implementa volar()
    pass
```

---

#### **4. I - Principio de Segregación de Interfaces (ISP)**  
> *"Los clientes no deben depender de interfaces que no usan"*.  

**Ejemplo malo**:  
```python
class Dispositivo:
    def imprimir(self):
        pass
    def escanear(self):  # ¿Y si el dispositivo no puede escanear?
        pass
```
**Ejemplo correcto**:  
```python
class Impresora:
    def imprimir(self):
        pass

class Escaner:
    def escanear(self):
        pass

class Multifuncional(Impresora, Escaner):  # Solo implementa lo necesario
    pass
```

---

#### **5. D - Principio de Inversión de Dependencias (DIP)**  
> *"Depende de abstracciones, no de implementaciones concretas"*.  

**Ejemplo malo**:  
```python
class MySQLDatabase:  # Dependencia concreta
    def guardar(self, datos):
        pass

class App:
    def __init__(self):
        self.db = MySQLDatabase()  # Acoplado a MySQL
```
**Ejemplo correcto**:  
```python
class Database(ABC):  # Abstracción
    @abstractmethod
    def guardar(self, datos):
        pass

class MySQLDatabase(Database):
    def guardar(self, datos):
        pass

class App:
    def __init__(self, db: Database):  # Depende de la abstracción
        self.db = db
```

---

### 🔹 **¿Por qué seguir SOLID?**  
✅ **Reduce acoplamiento** entre componentes.  
✅ **Facilita pruebas unitarias** y mantenimiento.  
✅ **Permite escalar** el código sin miedo a romper funcionalidades.  

---

### 📚 **Ejemplo de la vida real**  
Imagina un **café**:  
- **SRP**: La máquina de café no debe también tostar pan.  
- **OCP**: Puedes añadir leche (extender) sin modificar la máquina.  
- **LSP**: Un café descafeinado debe poder usarse como café normal.  
- **ISP**: No obligues a todos a usar azúcar si no lo desean.  
- **DIP**: La taza depende de la interfaz "LíquidoBebible", no de "Café" directamente.  

---

### 🛠️ **Herramientas que ayudan a aplicar SOLID**  
- **Patrones de diseño** (Factory, Strategy, Observer).  
- **Inyección de dependencias**.  
- **Linters** como SonarQube o ESLint.  

¿Quieres profundizar en algún principio en particular? 😊