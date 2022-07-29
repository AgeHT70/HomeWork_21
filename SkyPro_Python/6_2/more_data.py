import pprint


# def get_score(income):
#     score_list = []
#     for income_values in income.values():
#         for score in income_values.get():
#             score_list.append(score)
#     return score_list


income = {'29/07/2022 09:19:37': {'asgh': 0},
          '29/07/2022 09:54:40': {'Андрей': 0},
          '29/07/2022 09:55:18': {'Андрей': 0},
          '29/07/2022 09:56:50': {'sdhga': 200},
          '29/07/2022 09:57:36': {'ASDHA': 0},
          '29/07/2022 09:58:55': {'Андрей': 0},
          '29/07/2022 10:01:16': {'Андрей': 10}}

# print(max(income, key=get_score(income)))
#

score_list = []
for income_values in income.values():
    for score in income_values.get():
        score_list.append(score)
print(score_list)
