"""
Problem: Longest Substring Without Repeating Characters
Description:
Given a string s, find the length of the longest substring without
repeating characters.

Requirements:

Implement a function length_of_longest_substring(s: str) -> int.

The function should return the length (an integer) of the longest
substring without repeating characters.

The solution should be efficient (ideally O(n) time).

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""


# sliding window
def length_of_longest_substring(s: str) -> int:
    if not s:  # maneja string vacío
        return 0
    max_len = 1  # es 1 porque el set se inicializa con 1 caracter

    for i in range(len(s)):
        current = set(s[i])  # comienza con el caracter actual
        for j in range(i + 1, len(s)):
            if s[j] not in current:
                current.add(s[j])
                max_len = max(max_len, len(current))
            else:
                break
    return max_len

t1 = "abcabcbb"
t2 = "pwwkew"
t3 = "bbbbb"
t4 = "zzzzzadfezazzzz"
print("EXEC:", t1, "solution:", length_of_longest_substring(t1))
# print("EXEC:", t2, "solution:", length_of_longest_substring(t2))
# print("EXEC:", t3, "solution:", length_of_longest_substring(t3))
# print("EXEC:", t4, "solution:", length_of_longest_substring(t4))

# def length_of_longest_substring(s: str):
#     prev = ''.join(list(set(s))) # on avg this part should be O(n)
#     if not prev or len(prev) == 1:
#         print("-- no FOR loop happened")
#         return len(prev)
#     sl = len(s)
#     d = {}
#     sub_s = ""
#     for i in range(sl):
#         if len(sub_s) and (sub_s[len(sub_s) - 1] == s[i] or sub_s[0] == s[i]):
#             if sub_s[len(sub_s) - 1] == s[i]:
#                 sub_s = sub_s[0 : len(sub_s) - 1]
#             if len(sub_s) and sub_s not in d:
#                 print("-- valid sub_s found: ", sub_s)
#                 d[sub_s] = len(sub_s)
#             sub_s = s[i]
#         else:
#             sub_s += s[i]
#     r = 0
#     for v in d.values():
#         if v > r:
#             r = v
#     return r
