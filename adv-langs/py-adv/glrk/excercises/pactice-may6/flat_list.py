data = [[1, 2, 3], 4, 5, 6, [7,8]]

def f(l):
    r = []
    for e in l:
        if isinstance(e, list):
            r.extend(f(e))
        else:
            r.append(e)
    return r

print(f(data))


    