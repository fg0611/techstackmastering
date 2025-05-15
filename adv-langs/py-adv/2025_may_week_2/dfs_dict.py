# remove keys from structure of a given list
# FUNCIÓN remover_secret(diccionario):
#   PARA cada clave EN diccionario:
#     SI clave ES "secret":
#       ELIMINAR clave DE diccionario
#     SINO:
#       valor = diccionario[clave]
#       SI valor ES un diccionario:
#         remover_secret(valor) // Llamada recursiva
#       SINO SI valor ES una lista:
#         PARA cada elemento EN valor:
#           SI elemento ES un diccionario:
#             remover_secret(elemento) // Llamada recursiva
def remove_keys(key_list, data):
    if not data:
        return None
    if isinstance(data, dict):
        keys = [k for k in data]
        for k in keys:
            if k in key_list:
                del data[k]
            else:                
                remove_keys(key_list, data[k])
    if isinstance(data, list):
        for el in data:
            remove_keys(key_list, el)
    return data

d = {
    "username": "user",
    "secret": 123123,
    "users": [{"username": "user", "secret": "1234"}],
    "more_users": [[{"username": "user2", "secret": 3232}], {"password": 123123}]
}
print(remove_keys(["secret", "password"], d))
            
