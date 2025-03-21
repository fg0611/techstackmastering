# import companies
# import vacants
# import applications
# from candidates import data as candidates
# from skills import data as skills
# from candidates_skills import data as candidate_skills


# GETTING NUM OF VACANTS PER COMPANY
# vxc = [{**c, 'vacants': 0} for c in companies.data]
# for v in vacants.data:
#     for c in vxc:
#         if v['company'] == c['id']:
#             c['vacants'] += 1

# print(vxc)

# vacant_counts = {}
# for v in vacants.data:
#     cid = v['company']
#     vacant_counts[cid] = vacant_counts.get(cid, 0) + 1

# print(vacant_counts)

# for c in companies.data:
#     c['vacants'] = vacant_counts[c['id']]

# print(companies.data)

# for c in companies.data:
#     print(f'{c["name"]} has {c["vacants"]} vacants')

# print(vxc)

# companies = companies.data.copy()

# for v in vacants.data:
#     for c in companies:
#         if v['company'] == c['id']:
#             c['vacants'] = c.get('vacants', 0) + 1

# print(companies)

# GETTING NUM OF APPLICATIONS PER VACANT
# for v in vacants.data:
#     for a in applications.data:
#         if v['id'] == a['vacant']:
#             v['applications'] = v.get('applications', 0) + 1

# print(vacants.data)

# for k in vacants.data[0]:
#     print(k)
# print(vacants.data[0].keys())

# 
# for v in vacants.data:
#     v['applications'] = len([a for a in applications.data if a['vacant'] == v['id']])

# # print(vacants.data)

# keys_keep = ['title', 'applications']
# keys_remove = [k for k in vacants.data[0] if k not in keys_keep] 
# # print(keys_remove)
# for v in vacants.data:
#     for k in keys_remove:
#         # v.pop(k) # removes the key using method 
#         del v[k] # removes the key using dict access

# print(vacants.data)

# SKILLS PER CANDIDATE 
# for c in candidates:
#     c_skills = c.get('c_skills',0) # gen key c_skills
#     c['c_skills'] = len([cs for cs in candidate_skills if cs['candidate'] == c['id']])

# print(candidates)

# for c in candidates:
#     c_skills = c.get('c_skills',0) # gen key c_skills
#     c['c_skills'] = len(list(filter(lambda cs: cs['candidate'] == c['id'], candidate_skills)))

# print(candidates)

# skill_counts = {}
# for cs in candidate_skills:
#     candidate_id = cs['candidate']
#     skill_counts[candidate_id] = skill_counts.get(candidate_id, 0) + 1

# for c in candidates:
#     c['c_skills'] = skill_counts.get(c['id'], 0)

# print(candidates)