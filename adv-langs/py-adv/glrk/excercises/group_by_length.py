# Descripción:
# Escribe una función group_by_length(words)
#  que tome una lista de palabras y las agroupe en sub-listas según su longitud.

entrada = ["apple", "banana", "cat", "dog", "elephant", "fox"]
salida = [["cat", "dog", "fox"], ["apple"], ["banana", "elephant"]]
# Explicación:
# - Longitud 3: ["cat", "dog", "fox"]
# - Longitud 5: ["apple"]
# - Longitud 6: ["banana", "elephant"]


def group_by_length(l):
    d = {}
    for w in l:
        w_len = len(w)
        sub_list = d.setdefault(w_len, [w])
        if not w in sub_list:
            d[w_len].append(w)
    print(d)
    r = []
    for k in d.keys():
        r.append(d[k])
    return r

print(group_by_length(entrada))