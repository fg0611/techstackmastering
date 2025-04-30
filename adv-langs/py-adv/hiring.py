score_list = [12 , -12, 2, 2, 24, 1, 24]
# print(score_list)

# for i, n in enumerate(score_list):
#     print(i)




# sol 1
# score_list.sort()
# count = 0
# score_emp = score_list[0]
# for score in score_list:
#     if score > score_emp:
#         score_emp = score
#         count+=1
# print(count) 

# sol 2
# unique = set(score_list)
# print(len(unique)-1)

# kv_list = [{i : score} for i, score in enumerate(score_list)]
# print(kv_list)

# sol3
# unique = [score for i, score in enumerate(score_list) if score not in score_list[:i]]
# print(len(unique)-1)