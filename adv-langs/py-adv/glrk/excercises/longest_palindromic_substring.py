import re

def longest_palindromic_substring2(s: str) -> str:
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2    
    return s[start:end + 1]

def expand(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1  # Expande hacia la izquierda
        right += 1  # Expande hacia la derecha
    return right - left - 1  # Longitud del palíndromo

print(longest_palindromic_substring2("ababd"))

def longest_palindromic_substring(s: str) -> str:
    longest = ""
    s = re.sub(r'[^a-zA-Z]', '', s).lower()

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1] and len(sub_s) > len(longest):
                longest = sub_s
    return longest

# print(longest_palindromic_substring("A man, a plan, a canal: Panama"))
print(longest_palindromic_substring("ababd"))