# import random
# from vacants import data as vacants
# from skills import data as skills

# for each vacants we want to:
# - generate a random number (int) n_kills to be assigned
# - select randomly from skills list
# - assign those skills to vacant

# data = []

# for v in vacants:
#     n_skills = random.randint(1, 3)
#     random_skills = random.sample(skills, n_skills)
#     for rk in random_skills:
#         data.append({"id": len(data) + 1, "vacant": v["id"], "skill": rk["id"]})

# print(data)


# data = [
#     {"id": 1, "vacant": 1, "skill": 6},
#     {"id": 2, "vacant": 1, "skill": 14},
#     {"id": 3, "vacant": 2, "skill": 5},
#     {"id": 4, "vacant": 3, "skill": 6},
#     {"id": 5, "vacant": 3, "skill": 1},
#     {"id": 6, "vacant": 3, "skill": 8},
#     {"id": 7, "vacant": 4, "skill": 12},
#     {"id": 8, "vacant": 4, "skill": 5},
#     {"id": 9, "vacant": 5, "skill": 5},
#     {"id": 10, "vacant": 5, "skill": 2},
# ]

# import numpy as np

# data = []

# for v in vacants:
#     n_skills = np.random.randint(1, 3)
#     random_skills_indices = np.random.choice(len(skills), n_skills, replace=False)

#     for skill_index in random_skills_indices:
#         data.append(
#             {"id": len(data) + 1, "vacant": v["id"], "skill": skills[skill_index]["id"]}
#         )

# print(data)

data = [
    {"id": 1, "vacant": 1, "skill": 3},
    {"id": 2, "vacant": 2, "skill": 1},
    {"id": 3, "vacant": 2, "skill": 2},
    {"id": 4, "vacant": 3, "skill": 5},
    {"id": 5, "vacant": 3, "skill": 2},
    {"id": 6, "vacant": 4, "skill": 1},
    {"id": 7, "vacant": 5, "skill": 2},
]