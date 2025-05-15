def find_longest_substring_no_repeat(s):
    start = 0
    end = 0
    max_len = 0
    char_set = set()
    e = 0

    while end < len(s):
        e += 1
        if s[end] not in char_set:
            char_set.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
            char_set.remove(s[start])
            start += 1
    return max_len, e

data = 'acabcdefa'
print(find_longest_substring_no_repeat(data))