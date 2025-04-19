def calcular_tiempo_enfriamiento(cafe):
    if cafe.esta_caliente():
        # Lógica para calcular el enfriamiento
        print("Calculando tiempo de enfriamiento...")
    else:
        print("Este café ya está frío.")

class Cafe:
    def esta_caliente(self):
        return True

class Frapuchino(Cafe):
    def esta_caliente(self):
        return False

cafe_negro = Cafe()
frap = Frapuchino()

calcular_tiempo_enfriamiento(cafe_negro)  # Funciona bien
calcular_tiempo_enfriamiento(frap)       # Funciona, pero el mensaje es diferente. ¿Es esto un problema en nuestro contexto?