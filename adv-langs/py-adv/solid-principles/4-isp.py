# 4. **📌 ISP (Interface Segregation Principle
# - Principio de Segregación de Interfaces):**
#    *"No obligues a todos a usar azúcar si no lo desean."*
#    → Interfaces minimalistas: **azúcar** y **sin azúcar** son opciones separadas.

from abc import ABC, abstractmethod

class Cafe(ABC):
    @abstractmethod
    def servir(self):
        pass


class ConEndulzate(ABC):
    def __init__(self, dulce=False):
        self.dulce = dulce

    @abstractmethod
    def agregar_endulzante(self, dulce):
        pass


class ConLeche(ABC):
    def __init__(self, leche=False):
        self.leche = leche

    @abstractmethod
    def agregar_leche(self, leche):
        pass


class CafeNegro(Cafe, ConEndulzate):
    def __init__(self, dulce=False):
        super().__init__()
        self.dulce = dulce

    def agregar_endulzante(self):
        print("Si tiene endulzante" if self.dulce else "NO tiene endulzante")

    def servir(self):
        print("sirviendo CafeNegro...")


class CafeConLeche(Cafe, ConLeche, ConEndulzate):
    def __init__(self, leche=True, dulce=False):
        super().__init__()
        self.leche = leche
        self.dulce = dulce

    def agregar_leche(self):
        print("Si tiene leche" if self.dulce else "NO tiene leche")

    def agregar_endulzante(self):
        print("Si tiene endulzante" if self.dulce else "NO tiene endulzante")

    def servir(self):
        print("sirviendo Cafe con leche...")


# cafe = Cafe()
cafeNegro = CafeNegro(dulce=True)

cafeCLeche = CafeConLeche()

cafeCLecheDulce = CafeConLeche(dulce=True)


cafeNegro.servir()
cafeNegro.agregar_endulzante()


cafeCLeche.servir()
cafeCLeche.agregar_endulzante()

cafeCLecheDulce.servir()
cafeCLecheDulce.agregar_endulzante()
