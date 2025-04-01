import pandas as pd

def gen_qr(
    dev=True,
    bearer=None,
    commerce=None,
    amount=None,
    expiration=None,
    email=None,
    name=None,
    isPayable=False,
):
    """Genera un ID y una URL a partir de los datos de una fila."""
    # Ejemplo de lógica para generar ID y URL (reemplaza con tu lógica real)
    id_generado = f"ID-{commerce}-{amount}"
    url_generada = f"https://ejemplo.com/qr?id={id_generado}"
    return id_generado, url_generada

# Ejemplo de DataFrame
data = {'commerce': ['tienda1', 'tienda2', 'tienda3'],
        'amount': [0.1, 2, 10],
        'email': ['a@a.com','b@b.com','c@c.com'],
        'name': ['pepe','pipo','popo']}
df = pd.DataFrame(data)

# Listas para almacenar los resultados
ids = []
urls = []

# Iterar sobre las filas y llamar a gen_qr
for row in df.itertuples(index=False):
    id_generado, url_generada = gen_qr(commerce=row.commerce, amount=row.amount, email=row.email, name=row.name)
    ids.append(id_generado)
    urls.append(url_generada)

# Agregar los resultados al DataFrame
df['id'] = ids
df['qr'] = urls

print(df)

# import pandas as pd

# def generar_id_qr(fila):
#     """Genera un ID y una URL a partir de los datos de una fila."""
#     # Ejemplo de lógica para generar ID y URL (reemplaza con tu lógica real)
#     id_generado = f"ID-{fila['columna1']}-{fila['columna2']}"
#     url_generada = f"https://ejemplo.com/qr?id={id_generado}"
#     return id_generado, url_generada

# # Ejemplo de DataFrame
# data = {'columna1': [1, 2, 3],
#         'columna2': ['a', 'b', 'c']}
# df = pd.DataFrame(data)

# # Aplicar la función y crear las columnas "id" y "qr"
# df[['id', 'qr']] = df.apply(generar_id_qr, axis=1, result_type='expand')

# print(df)