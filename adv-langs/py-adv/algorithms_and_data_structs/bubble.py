# Bubble sort
# se hacen dos bucles donde el primero hace un recorrido principal
# el segundo es para comparar cada item con el siguiente y hacer intercambio de posiciones
# si resulta que se hizo todo un recorrido y no se ningun cambio entonces se corta la ejecucion

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = True
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

example = [17, 20, 23, 25, 31, 33, 48]

print(bubble_sort(example))