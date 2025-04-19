# 5. **📌 DIP (Dependency Inversion Principle - Principio de Inversión de Dependencias):**  
#    *"La taza depende de la interfaz 'LíquidoBebible', no de 'Café' directamente."*  
#    → La taza acepta **cualquier líquido** (té, café, chocolate) que cumpla la interfaz. 

from abc import ABC, abstractmethod

class LiquidoBebible(ABC):
    @abstractmethod
    def que_liquido_es():
        pass

class Cafe(LiquidoBebible):
    def __init__(self, tipo):
        self.tipo = tipo
    def que_liquido_es(self):
        return self.tipo

class Te(LiquidoBebible):
    def __init__(self, sabor):
        self.sabor = sabor
    def que_liquido_es(self):
        return self.sabor

class Jugo(LiquidoBebible):
    def __init__(self, fruta):
        self.fruta = fruta
    def que_liquido_es(self):
        return self.sabor

class Envase():
    def __init__(self, material):
        self.material = material
        self.contenido = None
    def llenar(self, liquido):
        self.contenido = liquido.que_liquido_es()
        print(f'El envase de {self.material} se esta llenando de {self.contenido}')
    def que_liquido_contiene(self):
        print(f'el envase contiene {self.contenido}')

cafe_br = Cafe('Café Brasileño')
# print(cafe_br.que_liquido_es())

envase = Envase(material='porcelana')

envase.llenar(cafe_br)

envase.que_liquido_contiene()

