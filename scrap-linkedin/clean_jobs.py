from pathlib import Path
import pandas as pd
import os

def remove_google_translate_urls_from_csv(filepath):
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath)
            df = df[~df["urls"].str.contains("translate.goog")]
            df = df[~df["urls"].str.contains("No URL found")]
            df.to_csv(filepath, index=False)
        except pd.errors.ParserError:
            print(f"El archivo '{filepath}' no es un CSV válido.")
            return None
        except Exception as e:
            print(f"No se pudo leer el archivo CSV: {e}")
            return None
    else:
        return None


fpath = Path("C:/Users/Francisco/Desktop/DEV_STUFF/APRENDIENDO/PROJECTS/repo/scrap-linkedin/linkedin-nest2.csv")


remove_google_translate_urls_from_csv(fpath)