# #Design a data structure that follows the constraints of a LRU (least-recently-usedclass LRUCache {
# # cap = 3 => a: 1, b: 1, c: 2 => d
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.cache.get(key, 0)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print(len(self.cache))
        if len(self.cache) == self.capacity:
            cache_filtered_by_vals = sorted(self.cache.items(), key=lambda item:item[1])
            self.cache.pop(cache_filtered_by_vals[0][0])
            self.cache.setdefault(key, value)
        else:
            self.cache.setdefault(key, value)


structure = LRUCache(capacity=3)

print(structure.get('a'))
print(structure.put('a', 1))
print(structure.put('b', 1))
print(structure.put('c', 1))
print(structure.put('d', 2))

print(structure.cache)


# Implement a function deep_omit(obj, keys) that removes specified keys and their corresponding values from an dictionary, including nested dictionary or lists.
data = {
    "name": "Alice",
    "password": "secret",
    "profile": {
        "age": 30,
        "password": "hidden",
        "preferences": {"theme": "dark", "password": "supersecret"},
    },
    'posts': [
        {'title': 'First Post', 'secret': True},
        {'title': 'Second Post', 'secret': False}
    ]
}

def deep_omit_verbose(obj, list_keys):
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            if k not in list_keys:
                new_obj[k] = deep_omit(v, list_keys)
        return new_obj
    elif isinstance(obj, list):
        new_list = []
        for el in obj:
            if el not in list_keys:
                new_list.append(deep_omit(el, list_keys))
        return new_list
    else:
        return obj

def deep_omit(obj, list_keys): # manas

    if isinstance(obj, dict):
            return { key: deep_omit(val, list_keys) for key, val in obj.items() if key not in list_keys }
    elif isinstance(obj, list):
            return [ deep_omit(val, list_keys) for val in obj]
    else:
        return obj
    
print(deep_omit_verbose(data, ["password", "secret"]))
print(deep_omit(data, ["password", "secret"]))
