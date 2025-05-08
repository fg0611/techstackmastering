# find path of keys and indexes to get to target value

data = {
    "a": 1,
    "b": {"c": 2, "d": [3, 4, {"e": 5}]},
    "f": [6, {"g": 7, "h": 8}]
}
target = 5

def find_target(structure, goal, path=[]):
    if isinstance(structure, dict):
        for k, v in structure.items():
            current_path = path + [k]
            result = find_target(v, goal, current_path)
            if result:
                return result
    elif isinstance(structure, (list, tuple)):
        for i, v in enumerate(structure):
            current_path = path + [i]
            result = find_target(v, goal, current_path)
            if result:
                return result
    elif structure==target:
        return path
    return None

print(find_target(data, target))