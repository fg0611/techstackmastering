import json
datos = {'nombre': 'Juan', 'edad': 30}
json_str = json.dumps(datos)

print(json_str)

print(json.loads(json_str))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

@staticmethod
def metodo_estatico():
    print("Método estático")

@classmethod
def metodo_de_clase(cls):
    print(f"Método de clase: {cls}")