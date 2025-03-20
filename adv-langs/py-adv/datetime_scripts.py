# Módulo datetime
import datetime

# El módulo datetime es el principal para trabajar con fechas y horas en Python. 
# Contiene varias clases, siendo las más importantes:

# datetime: Representa una fecha y hora combinadas.
# date: Representa una fecha (año, mes, día).
# time: Representa una hora (horas, minutos, segundos, microsegundos).
# timedelta: Representa una duración, la diferencia entre dos fechas o horas.

now = datetime.datetime.now()
today = datetime.datetime.today()
print(now)
print(today)
date = datetime.date(2022, 1, 5)
print(date)
time = datetime.time(12, 0, 0)
print(time)

time_to_today = datetime.datetime.combine(today, time)

time_difference = today - time_to_today
print(time_difference.total_seconds()/60/60)