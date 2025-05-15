def findWord(arr):
    # split arr into pairs
    subs = [e.split('>') for e in arr]
    
    result = []
    count = 20

    # loop through 
    while subs and count != 0:
        count -= 1
        if not result:
            result.append(subs[0])
            subs.remove(subs[0])
        else:
            for pair in subs:
                # 1st char in result starting pair equal to 2nd char in pair
                if result[0][0] == pair[1]:
                    # inser at beggining and remove from subs
                    result.insert(0, pair)
                    subs.remove(pair)
                # final char of result equals 1st char on pair 
                elif result[-1][1] == pair[0]:
                    # insert at end and remove from subs
                    result.append(pair)
                    subs.remove(pair)
    
    r = [el[0] for el in result[:-1]] + result[-1]

    return ''.join(r)

r = findWord(["I>N", "A>I", "P>A", "S>P"]) 
# sp pa ai in
print(r)

r2 = findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])
print(r2)
# po or rt tu ug ga al
# findWord(["P>E", "E>R", "R>U"])

# findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) // HUNGARY
# findWord(["I>F", "W>I", "S>W", "F>T"]) // SWIFT
r3 = findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])
print(r3)