# Exercise: Counting Words in a Text

# Write a function called count_words that takes a text string
#  as input and returns a dictionary where the keys are the unique words
#  found in the text (converted to lowercase) and the values ​​are the number
#  of times each word appears.

texto = "El perro ladra fuerte. El gato también ladra."
# {'el': 2, 'perro': 1, 'ladra': 2, 'fuerte': 1, 'gato': 1, 'también': 1}

def count_words(phrase: str):
    import re
    phrase = phrase.lower()
    d = {}
    l = phrase.split()
    l = [re.sub(r'[^\w\s]', '', w) for w in l]
    for w in l:
        d.setdefault(w, 0)
        if w in d.keys():
            d[w] += 1
            
    return d


print(count_words(texto))