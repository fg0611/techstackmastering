# import random as rnd
# import datetime as dt
# from candidates import data as candidates
# from vacants import data as vacants


# generate random datetime from range start-end
# start = dt.datetime.strptime("2024-11-01", "%Y-%m-%d")
# end = dt.datetime.strptime("2025-03-01", "%Y-%m-%d")


# print(dt.timedelta(end-start))
# def random_datetime(start: dt.datetime, end: dt.datetime):
#     if end <= start:
#         print("Error in time range")
#     res = start + dt.timedelta(days=rnd.randint(0, (end - start).days))
#     # print(res)
#     return res.strftime("%Y-%m-%d")


# random_datetime(start, end)


# list of candidates who applied for the job position (id, company, vacant)
# data = []

# for c in candidates:
#     n_apply = rnd.randint(1, 3)  # times candidate applied
#     c_vacants = rnd.sample(
#         vacants, min(n_apply, len(vacants))
#     )  # select random vacants for candidate
#     for cv in c_vacants:
#         data.append(
#             {
#                 "id": len(data) + 1,
#                 "candidate": c["id"],
#                 "vacant": cv["id"],
#                 "application_date": random_datetime(start, end),
#             }
#         )

# print(data)

# LIST OF APPLICATIONS USING RANDOM DATA PYTHON + RANDOM
data = [
    {"id": 1, "candidate": 1, "vacant": 3, "application_date": "2025-01-08"},
    {"id": 2, "candidate": 1, "vacant": 2, "application_date": "2024-11-20"},
    {"id": 3, "candidate": 1, "vacant": 5, "application_date": "2025-02-11"},
    {"id": 4, "candidate": 2, "vacant": 3, "application_date": "2024-12-06"},
    {"id": 5, "candidate": 3, "vacant": 4, "application_date": "2024-11-26"},
    {"id": 6, "candidate": 4, "vacant": 1, "application_date": "2025-01-27"},
    {"id": 7, "candidate": 4, "vacant": 5, "application_date": "2024-11-24"},
    {"id": 8, "candidate": 5, "vacant": 1, "application_date": "2024-11-10"},
    {"id": 9, "candidate": 5, "vacant": 2, "application_date": "2024-12-15"},
    {"id": 10, "candidate": 5, "vacant": 3, "application_date": "2024-11-13"},
]