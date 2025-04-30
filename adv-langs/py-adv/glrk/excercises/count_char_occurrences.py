# texto = "Hi Fran, you good?"
texto = "hello world"

def count_char_occurrences(t: str):
    d:dict = {}
    t = t.replace(' ', '').lower()
    for l in t:
        d[l] = d.get(l, 0) + 1 
    return d

print(count_char_occurrences(texto))

# def count_char_occurrences(t: str):
#     d = {}
#     t = t.replace(' ', '').lower()
#     for l in t:
#         d.setdefault(l, 0)
#         if l in t:
#             d[l] += 1 
#     return d
