# Problema: Dado un array de números y un tamaño de
# ventana K, encontrar la suma máxima de cualquier
# subarray de tamaño K.

entry = [1, 3, 5, 4, 6, 0, 8, 2, 4]
size = 2

def find_k(l, k):
    start, end = 0, k - 1
    result, current_sum = sum(l[0:k]), sum(l[0:k])
    for i in range(k, len(l)):  # starts at next number
        i_pop = i - k
        current_sum = current_sum - l[i_pop] + l[i]
        if current_sum > result:
            start = i_pop + 1
            end = i
            result = current_sum
    return start, end, result


print(find_k(entry, size))
