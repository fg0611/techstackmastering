import companies
import vacants
import applications

# GETTING NUM OF VACANTS PER COMPANY
# vxc = [{**c, 'vacants': 0} for c in companies.data]
# for v in vacants.data:
#     for c in vxc:
#         if v['company'] == c['id']:
#             c['vacants'] += 1

# print(vxc)

# companies = companies.data.copy()

# for v in vacants.data:
#     for c in companies:
#         if v['company'] == c['id']:
#             c['vacants'] = c.get('vacants', 0) + 1

# print(companies)

# for v in vacants.data:
#     for a in applications.data:
#         if v['id'] == a['vacant']:
#             v['applications'] = v.get('applications', 0) + 1

# print(vacants.data)

# for k in vacants.data[0]:
#     print(k)
# print(vacants.data[0].keys())

for v in vacants.data:
    v['applications'] = len([a for a in applications.data if a['vacant'] == v['id']])

# print(vacants.data)

keys_keep = ['title', 'applications']
keys_remove = [k for k in vacants.data[0] if k not in keys_keep] 
# print(keys_remove)
for v in vacants.data:
    for k in keys_remove:
        # v.pop(k) # removes the key using method 
        del v[k] # removes the key using dict access

print(vacants.data)