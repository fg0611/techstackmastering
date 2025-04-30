# Problem:
# Write a function group_anagrams(words) 
# that takes a list of strings and groups them into sub-lists of anagrams. For example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# w = 'cba'
# print(w)
# print(''.join(sorted(w)))

# with a dictionary with setdefault
def group_anagrams(words):
    d = {}
    for w in words:
        sw = ''.join(sorted(w)) # here we create sorted word which will define the key
        dk = d.setdefault(sw, [w]) # part is important because setdefault returns sub_array 
        # or just creates the key:val pair in this case with predefined list loaded with the word  
        if w not in dk: # dk is the sub_list so in the dict would be key=sw and val=dk  
            # we check if the word isn't there and push it to dk[]
            d[sw].append(w)
    # next part takes every dict value which are lists and pushes them to resulting list
    r = []
    for k in d.keys(): 
        r.append(d[k])
    return r

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# def group_anagrams(words):
#     d = {}
#     for w in words:
#         sw = ''.join(sorted(w))
#         if sw not in d.keys():
#             d[sw] = [w]
#         else:
#             d[sw].append(w)
#     r = []
#     for k in d.keys():
#         r.append(d[k])
#     return r

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# for k in {'a':1}.keys():
#     print(k)


# def group_anagrams(words, result=None):
#     if not isinstance(result, list):
#         result = []
#     if not words:
#         return result;
#     w = words[0]
#     words.pop(0)
#     sub_list = [w]
#     for i, el in enumerate(words):
#         if sorted(w) == sorted(el):
#             sub_list.append(el)
#             words.pop(i)
#     result.append(sub_list)
#     return group_anagrams(words, result)

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# def group_anagrams(words, result = []):    
#     """
#     Takes a list of words and separates them in anagram groups inside a new resulting list
#     """
#     if not isinstance(words, list) or not words:
#         print("arg must be a List and not an empty one or process completed")
#         return result;
#     else:
#         w = words[0]
#         words.pop(0)
#         sub_list = [w]
#         for i, sw in enumerate(words):
#             if (len(set(w) & set(sw)) == len(set(w))):
#                 sub_list.append(sw)
#                 words.pop(i)
#         result.append(sub_list)                
#         return group_anagrams(words, result)

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    # for w in words:
    #     w1 = set(w)
    #     words = [el for el in words if el != w]
    #     sub_list.append(w)
    #     for subw in words:
    #         w2 = set(subw)
    #         comp = len(w1) & len(w2) == len(w1) 
    #         if comp:
    #             words = [el for el in words if el != subw]
    #             sub_list.append(subw)
    #     result.append(sub_list)
    #     sub_list = []
    # return result

# s1 = 'eat'
# s2 = 'ate'
# r = len(set(s1) & set(s2)) == len(s1)

# print(r)
