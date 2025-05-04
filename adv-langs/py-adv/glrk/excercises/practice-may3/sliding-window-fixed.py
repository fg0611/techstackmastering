# tamaño fijo
# Ejemplo 1: Suma máxima de subarray de tamaño fijo (K)
# Problema: Dado un array de números y un tamaño de ventana K,
# encontrar la suma máxima de cualquier subarray de tamaño K.
# Ejemplo:
# arr = [2, 1, 5, 1, 3, 2]
arr = [2, 3, 2, 5, 1, 5]
# arr = [2, 1, 5]
k = 3

def max_sum_subarr(arr, k):

    if len(arr) < k + 1:
        return sum(arr)
    start = 0
    end = k - 1
    curr_sum = sum(arr[:k])
    print("init ->", start, end, arr[start : end + 1], curr_sum)

    for ws in range(1, len(arr) - 1):
        we = ws + k - 1
        if we <= len(arr) - 1:
            w_sum = curr_sum - arr[ws - 1] + arr[we]
            if w_sum > curr_sum:
                start = ws
                end = we
            curr_sum = w_sum
        else:
            break

    print("result -> ", start, end, arr[start : end + 1], curr_sum)
    return curr_sum


print(max_sum_subarr(arr, k))

# tamaño variable
