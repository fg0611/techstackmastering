# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

entry = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagrams(l):
    d = {}

    for w in l:
        sw = "".join((sorted(w)))
        print(sw)
        d.setdefault(sw, [w])
        if w not in d[sw]:
            d[sw].append(w)
    r = []
    for k in d.keys():
        r.append(d[k])
    return r

print(anagrams(entry))