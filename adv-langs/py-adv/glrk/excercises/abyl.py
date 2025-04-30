# Write a function that takes a list of words 
# and an integer representing a length. 
# The function should return a list of lists, where each sublist contains 
# all the anagrams from the original list that have the specified length.

def abyl(arr, long):
    d = {}
    for w in arr:
        sw = ''.join(sorted(w))
        if len(sw) == long:
            d.setdefault(sw, []).append(w)
    
    r = [v for v in d.values() if len(v)>1]
    return r
        


# Ejemplo de uso:
entry = ["amor", "roma", "omar", "azar", "rata", "atar", "arte", "tear", "rate"]
l = 4
r = abyl(entry, l)
print(r)
