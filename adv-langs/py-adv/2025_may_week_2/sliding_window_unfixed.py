# find longest substring with no repeated letters
def sw_unfixed(ls):    
    if not ls:
        return None
    long = 1
    start = 0
    i = 1
    e = 0

    while i < len(ls):
        e+=1
        if ls[start] != ls[i]:
            long = max(long, len(ls[start:i+1]))
            i += 1
        else:
            start += 1
            i = start+1
    
    return long, e

data = 'acabcdefa'
print(sw_unfixed(data))
