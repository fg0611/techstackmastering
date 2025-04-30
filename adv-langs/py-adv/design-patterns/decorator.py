def agregar_sabor(sabores):
    def accion(funcion_original):
        def funcion_mod():
            return f'{funcion_original()} {" ".join(sabores)}'
        return funcion_mod
    return accion

@agregar_sabor(['choc', 'vainilla', 'fresa'])
def armar_helado():
    return 'helado de : '

print(armar_helado())