#  python 🐍

directory = {
    "raiz": {
        "documentos": {
            "informe.txt": {"tamaño": "10KB", "tipo": "texto", "metadata": [1, 2, 3]},
            "presentacion.pptx": {"tamaño": "2MB", "tipo": "presentacion"},
        },
        "imagenes": {
            "foto1.jpg": {"tamaño": "500KB", "tipo": "imagen"},
            "logo.png": {"tamaño": "100KB", "tipo": "imagen"},
        },
        "usuario.dat": {"tamaño": "5KB", "tipo": "binario"},
    }
}

def map_all(folders, level=1):
    if isinstance(folders, dict):
        if "tamaño" in folders: # here there is a file so just print complete dict
            print(f'{level * " "} {folders}')
        else:
            for k,v in folders.items():
                    print(f'{level * " "}/{k}')
                    map_all(v, level + 1)

map_all(directory)


#  files smaller than 100kb nad it's location
# def map_dir(fs, path="", result=None):
#     if result is None:
#         result = []
#     if isinstance(fs, dict):
#         for k, v in fs.items():
#             if k == "tamaño" and "KB" in v:
#                 if int(v.replace("KB", "")) < 100:
#                     result.append({"path": path, "size": v, "type": fs.get("tipo", "unknown")})
#             else:
#                 new_path = f'{path}/{k}' if path else k
#                 map_dir(v, new_path, result)               
#     return result


# print(map_dir(directory))
