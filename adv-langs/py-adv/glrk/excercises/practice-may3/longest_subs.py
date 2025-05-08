def longest_substring_no_repeats(text):
    result = {}
    for i in range(len(text) - 1):

        d = {text[i]: i}

        for j in range(i + 1, len(text)):
            if text[j] in d:
                if len(d) > len(result):
                    result = d.copy()
                    d.clear()
                break
            else:
                d[text[j]] = j
                if i == len(text) - 2 and len(d) > len(result):
                    result = d.copy()

    print(result)
    return len(result)


# Ejemplo:
# s = "bbabcabc"
s = "ccca"
print(longest_substring_no_repeats(s))  # Output: 3 ("abc")
