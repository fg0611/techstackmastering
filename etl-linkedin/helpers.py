import re
from datetime import datetime, timedelta


# Función para convertir a días
def days_published(text):
    if not isinstance(text, str):
        return 0
    text = text.lower()  # Convertir a minúsculas para manejar mayúsculas y minúsculas
    # Extraer el número usando una expresión regular
    numero = int(re.search(r"\d+", text).group())

    # Determinar la unidad de tiempo
    if "día" in text or "dia" in text or "day" in text:
        return numero
    elif "semana" in text or "week" in text:
        return numero * 7
    elif "mes" in text or "month" in text:
        return numero * 30
    else:
        return 0  # Si no se reconoce el formato


def date_published(days):
    if not isinstance(days, int):
        return None
    today = datetime.today()
    return (today - timedelta(days=days)).strftime("%m-%d-%Y")


def extract_num_from_str(txt):
    if not isinstance(txt, str):
        return None
    num = re.search(r"\d+", txt)
    if num:
        return num.group()
    return None
    # else:
    #     print(f"String: {txt} -> No se encontró ningún número.")
