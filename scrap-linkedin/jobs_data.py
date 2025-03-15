# palabras reservadas de python
# False, True, None, and, or, not, if, elif, else, for,
#  while, break, continue, return, def, class, try, except, finally,
#  import, from, as, global, nonlocal, lambda, yield, with, async, await

import re
from scripts.csv_handler import manage_job_csv, csv_to_df  #
from scripts.job import job_search  #

search_query = "nest.js"
filebase = f'{re.sub(r"^a-zA-Z0-9", "", search_query.replace(" ", ""))}.csv'  # deja solo num y letras en el filename
l_filename = f"linkedin-{filebase}"
j_filename = f"jobs-{filebase}"

df = csv_to_df(l_filename)
# df = df['urls'].apply(fix_url) # esta linea solo se aplica si las url son complejas pero ya estan arregladas en el manage_csv

print(df.head(1))

# df = df.drop_duplicates() esto ya no se haria porque ya se estan manejando duplicados en el manage_csv

if df is not None:
    print("Archivo cargado correctamente:")
    print(df.head(1))
    # Suponiendo que ya tienes un DataFrame llamado df
    linkedin_urls = df.iloc[:, 0]  # Esto accede a la primera columna (todas las filas, columna 0)

    # print(linkedin_urls[0:2])

    for url in linkedin_urls:
        job_info = job_search(url)
        if (len(job_info) > 0):
            manage_job_csv(job_info, j_filename)      
                          
else:
    print("Hubo un error al cargar el archivo.")
