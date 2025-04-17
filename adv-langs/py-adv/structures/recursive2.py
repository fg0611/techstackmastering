sistema_archivos = {
    "directorio": "raiz",
    "elementos": [
        {
            "directorio": "documentos",
            "elementos": [
                {"archivo": "informe.txt"},
                {"archivo": "presentacion.pptx"},
            ],
        },
        {
            "directorio": "imagenes",
            "elementos": [
                {"archivo": "foto1.jpg"},
                {"archivo": "foto2.png"},
                {
                    "directorio": "vacaciones",
                    "elementos": [
                        {"archivo": "foto3.jpg"},
                        {"archivo": "foto4.png"},
                        {
                            "directorio": "oficina",
                            "elementos": [
                                {"archivo": "foto5.jpg"},
                                {"archivo": "foto6.png"},
                            ],
                        },
                    ],
                },
            ],
        },
        {"archivo": "notas.txt"},
    ],
}

kd = "directorio"
ke = "elementos"
ka = "archivo"


def rev_dir(data, indent):
    if kd in data:
        print(f"{indent} {kd}: {data[kd]}")
        if data.get(ke, []):
            for e in data[ke]:
                rev_dir(e, indent + "   ")
    elif ka in data:
        print(f"{indent} {ka} -> {data[ka]}")


# rev_dir(sistema_archivos, "")


def buscar_arch(data, nombre):
    ke = "elementos"
    ka = "archivo"
    if data.get(ka, "") == nombre:
        return data[ka]
    if data.get(ke, []):
        for e in data[ke]:
            res = buscar_arch(e, nombre)
            if res:
                return res
    else:
        return None


# print(buscar_arch(sistema_archivos, "foto3.jpg"))
# print(buscar_arch(sistema_archivos, "foto12.jpg"))


# Escribe una función recursiva que cuente el número total de archivos en el sistema de archivos.
def contar_arch(data):
    cant = 0
    if data.get(ka, {}):
        cant += 1
    elif data.get(ke, []):
        for el in data[ke]:
            cant += contar_arch(el)
    return cant


# print(contar_arch(sistema_archivos))


# Escribe una función recursiva que encuentre el directorio que contiene el mayor número de archivos.
def buscar_dirs(data, dirs={}):
    if data.get(kd, ""):
        dirs[data[kd]] = data[ke]
    if data.get(ke, []):
        for e in data[ke]:
            buscar_dirs(e, dirs)
    return dirs


# print(buscar_dirs(sistema_archivos)['vacaciones'])
def conteo_arch(data):
    cant = 0
    if data.get(ka):
        cant += 1
    elif data.get(ke):
        for e in data[ke]:
            cant += conteo_arch(e)
    return cant


# print(conteo_arch(sistema_archivos))


# print(arch_dir(sistema_archivos))


def arch_dir(data):
    # hacer el dict con data de dirs
    kdata = buscar_dirs(data)
    result = {}
    # recorrer las keys y calcular los archivos por dir
    for klist in kdata:
        for e in kdata[klist]:
            result[klist] = result.get(klist, 0) + conteo_arch(e)
    return result

print(arch_dir(sistema_archivos))

# kdata = buscar_dirs(sistema_archivos)


# print(kdata['vacaciones'])

# Escribe una función recursiva que devuelva una lista con la ruta completa de cada archivo
#  en el sistema de archivos.
