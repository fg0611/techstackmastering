# dado un arr de enteros retorne las tripletas que sumen 0
# no se pueden repetir tripletas

entry = [-1, 0, 1, 2, -1, 4]
# out = [[-1, -1, 2], [-1, 0, 1]]


def solution(l):
    l.sort()  # O(n log n)

    sett = set()

    for i in range(len(l) - 2):
        left = i+1
        right = len(l) - 1
        
        while left < right:
            total = l[i] + l[left] + l[right]
            if  total == 0:
                sett.add(tuple([l[i], l[left], l[right]]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return [list(x) for x in sett]

print(solution(entry))
