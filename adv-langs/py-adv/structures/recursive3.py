def cuenta_regresiva(n):
    """Cuenta regresiva recursiva desde n hasta 0."""
    if n == 0:  # Caso base: detener la recursión cuando n llega a 0
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)  # Llamada recursiva con n-1

# Ejemplo de uso
cuenta_regresiva(5)