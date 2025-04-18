# from abc import abstractmethod

class Vehiculo:
    def llenarTanque (self, tipoVehiculo):
        tipoVehiculo.llenarTanque()

class Auto:
    def llenarTanque (self):
        print('llenando con gasolina')

class Avion:
    def llenarTanque (self):
        print('llenando con comb p/avion')

vehiculo = Vehiculo()

print(vehiculo.llenarTanque(Auto()))
print(vehiculo.llenarTanque(Avion()))

# class Vehiculo:
#     def llenarTanque(self, tipo):
#         if tipo == 'auto':
#             print('c gasolina')
#         elif tipo == 'avion':
#             print('c c/avion')
#         else:
#             print('vehiculo indef en esta clase')

# v = Vehiculo()

# print(v.llenarTanque('buque'))


# def pago(t):
#     if t == "tdc":
#         print("pago c tdc")
#     elif t == "efec":
#         print("pago c efec")
#     elif t == "deb":
#         print("pago c deb")
#     else:
#         print("no existe ese metodo d pago")

# pago('lo que sea')

# def tdc ():
#     print('pago c tdc')
# def efec ():
#     print('no lo acepta')
# def deb ():
#     print('pago c deb')
# def chapas ():
#     print('pago c chapas')

# def pos (tipoPago):
#     tipoPago()

# pos(chapas)

