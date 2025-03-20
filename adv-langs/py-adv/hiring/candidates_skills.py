# import random
# from skills import data as skills
# from candidates import data as candidates

# # print(skills)

# data = []

# for c in candidates:
#     num_skills = random.randint(1, 4)  # Genera un número aleatorio de skills (0-4)
#     skills_assigned = random.sample(
#         skills, min(num_skills, len(skills))
#     )  # Selecciona skills aleatorios
#     for sa in skills_assigned:
#         data.append({"id": len(data) + 1, "candidate": c["id"], "skill": sa["id"]})

# print(data)

data = [
    {"id": 1, "candidate": 1, "skill": 13},
    {"id": 2, "candidate": 1, "skill": 7},
    {"id": 3, "candidate": 2, "skill": 12},
    {"id": 4, "candidate": 2, "skill": 9},
    {"id": 5, "candidate": 2, "skill": 3},
    {"id": 6, "candidate": 2, "skill": 6},
    {"id": 7, "candidate": 3, "skill": 4},
    {"id": 8, "candidate": 3, "skill": 3},
    {"id": 9, "candidate": 3, "skill": 11},
    {"id": 10, "candidate": 4, "skill": 14},
    {"id": 11, "candidate": 4, "skill": 9},
    {"id": 12, "candidate": 4, "skill": 6},
    {"id": 13, "candidate": 4, "skill": 13},
    {"id": 14, "candidate": 5, "skill": 2},
    {"id": 15, "candidate": 5, "skill": 12},
]
