list_nums = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]

# flatten a list


def flat(l):
    # r = []
    if isinstance(l, list):
        # for el in l:
        #     if isinstance(el, list):
        #         r.extend(flat(el))
        #     else:
        #         r.append(el)
        return [item for el in l for item in flat(el)] if isinstance(l, list) else [l]
    else:
        return [l]

    
print(flat(list_nums))
