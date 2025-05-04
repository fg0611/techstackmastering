# dado un arr de enteros retorne las tripletas que sumen 0
# no se pueden repetir tripletas

entry = [-1, 0, 1, 2, -1, 4]
# out = [[-1, -1, 2], [-1, 0, 1]]

def solution(l):
    d = {}

    for i in range(0, len(l)):
        for j in range(1, len(l)):
            for k in range(2, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    d.setdefault(tuple(sorted([l[i] , l[j] , l[k]])), 0)
    

    return [list(x) for x in d]

print(solution(entry))