# def count_anagrams(l):
#     d = {}
#     for w in l:
#         sw = ''.join(sorted(w))
#         d[sw] = d.get(sw, 0) + 1
#     return d

# # # Test cases
# entry = ["eat", "tea", "tan", "ate", "nat", "bat"]
# def test_cases():
#     print(count_anagrams(entry))

# test_cases()