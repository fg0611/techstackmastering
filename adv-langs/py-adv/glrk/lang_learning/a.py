# def first_unique_char(s: str) -> int:
#     # Your solution here
#     count = 0
#     for l in s:
#         for sl in s:
#             if l == sl:
#                 count += 1
#         if count == 1:
#             return s.find(l)
#         count = 0
#     return -1

# # Test cases
# def test_cases():
#     print(first_unique_char("leetcode"))  # Should return 0
#     print(first_unique_char("loveleetcode"))  # Should return 2
#     print(first_unique_char("aabb"))  # Should return -1

# test_cases()

# def is_anagram(s: str, t: str) -> bool:
#     # Your solution here
#     # return sorted(s) == sorted(t)
#     if len(s) != len(t):
#         return False
#     # primero crear un diccionario que contendra los conteos de letras
#     char_count = {}
#     # recorre el string y va sumando los caracteres en la key que corresponde
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     # luego hace el recorrido del otro string
#     # 1 - revisa si la letra existe, si no existe return False
#     # 2 - existe, entonces las cuenta y compara con el diccionario
#     for char in t:
#         exists = char_count.get(char, 0)
#         if not exists or exists != t.count(char):
#             return False
#     return True

def is_anagram(s: str, t: str) -> bool:
    # Your solution here
    # return sorted(s) == sorted(t)
    if len(s) != len(t):
        return False
    # primero crear un diccionario que contendra los conteos de letras
    char_count = {}
    # recorre el string y va sumando los caracteres en la key que corresponde
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    # ir verificando si la letra es una key
    # si lo es entonces restar al contador de la key 1
    # verificar el value de la key es 0 y si lo es hacer un delete del dict
    # ver si ya no hay keys en el dict de ser asi entonces retornar True
    for char in t:
        if char in char_count:
            char_count[char] -= 1
            if char_count.get(char, 0) == 0:
                del char_count[char]
    if len(char_count):
        return False
    return True
    

# Test cases
def test_cases():
    print(is_anagram("anagram", "nagaram"))  # Should return True
    print(is_anagram("rat", "car"))  # Should return False
    print(is_anagram("listen", "silent"))  # Should return True
    print(is_anagram("hello", "world"))  # Should return False


test_cases()

# d = {'a': 1, 'g': 2}
# for k, v in enumerate(d):
#     print(f'{k}/{v}')


