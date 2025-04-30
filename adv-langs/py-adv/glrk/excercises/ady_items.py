

def ady(l):
    result = []
    group = [l[0]]

    for i in range(1, len(l)):
        if l[i-1] == l[i]:
            group.append(l[i])
            print(group)
        else:
            result.append(group)
            group = [l[i]]
        if i == len(l)-1:
            result.append(group)

    return result

e = [1, 1, 1, 2, 2, 1, 1, 3, 3]

print(ady(e))
     
