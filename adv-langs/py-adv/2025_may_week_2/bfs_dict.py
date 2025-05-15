from collections import deque

def remove_keys(key_list, data):
    if not data:
        return None
    q_data = deque([data])

    while q_data:
        q_el = q_data.popleft()
        if isinstance(q_el, dict):
            keys = [k for k in q_el]
            for k in keys:
                if k in key_list:
                    del q_el[k]
            for v in q_el.values():
                if isinstance(v, list):
                    q_data.append(v)
        elif isinstance(q_el, list):
            for list_el in q_el:
                q_data.append(list_el)                
    return data

d = {
    "username": "user",
    "secret": 123123,
    "users": [{"username": "user", "secret": "1234"}],
    "more_users": [[{"username": "user2", "secret": 3232}], {"password": 123123}]
}
print(remove_keys(["secret", "password"], d))
            
