
from functools import lru_cache
import time

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(20):
    print(fib(i),end='..')





# def find_common_ingredients(recipe_1, recipe_2):
#     finalval = []
#     for rece1 in recipe_1:
#         if rece1 in recipe_2 and rece1 not in finalval:
#             finalval.append(rece1)
#     return (finalval)
    # final_val=[]
    # for reci1 in recipe_1:
    #     for reci2 in recipe_2:
    #         if reci1==reci2 :
    #             final_val.append(reci2)
    # if len(final_val)>1:
    #     lens=len(recipe_2)
    #     return final_val
    # else:return -1
# print(find_common_ingredients([1,1,1,2,3],[1,5,2]))