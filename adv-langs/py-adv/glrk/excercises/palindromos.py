# palndormos
def palin(t: str) -> str:
    t = t.replace(" ", "")
    r = ''
    for i in range(len(t)):
        for j in range(i+1, len(t)+1):
            subs = t[i:j]
            if subs == subs[::-1] and len(subs)>len(r):
                r = subs
    return r


print(palin("a man a plan a canal panama"))
