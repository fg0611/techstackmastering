data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sw_fixed(ls, k):
    
    if k >= len(ls):
        return None    
    return [ls[i:i+k] for i in range(len(ls)-k+1)]

print(sw_fixed(data, 3))

