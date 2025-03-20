# import random
# from candidates import data as candidates
# from vacants import data as vacants

# # list of candidates who applied for the job position (id, company, vacant)
# data = []

# for c in candidates:
#     n_apply = random.randint(1, 3)  # times candidate applied
#     c_vacants = random.sample(
#         vacants, min(n_apply, len(vacants))
#     )  # select random vacants for candidate
#     for cv in c_vacants:
#         data.append({"id": len(data) + 1, "candidate": c["id"], "vacant": cv["id"]})

# print(data)

data = [
    {"id": 1, "candidate": 1, "vacant": 2},
    {"id": 2, "candidate": 1, "vacant": 5},
    {"id": 3, "candidate": 1, "vacant": 3},
    {"id": 4, "candidate": 2, "vacant": 2},
    {"id": 5, "candidate": 3, "vacant": 4},
    {"id": 6, "candidate": 3, "vacant": 1},
    {"id": 7, "candidate": 3, "vacant": 2},
    {"id": 8, "candidate": 4, "vacant": 1},
    {"id": 9, "candidate": 4, "vacant": 4},
    {"id": 10, "candidate": 4, "vacant": 5},
    {"id": 11, "candidate": 5, "vacant": 5},
]
