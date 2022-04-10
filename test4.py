# class Count:
#     def __init__(self,start,end):
#         self.start=start
#         self.end =end
#         self.count=0
#
#     def __iter__(self):
#         while self.count<self.end:
#             self.count+=1
#             yield self.count
# t=Count(0,30)
# iter_val=iter(t)
# for val in iter_val:
#     print(val)

list1=[1,2,3,2,1]
list2=[2,2,1,5,6]
final_val=[]
for list_val in list1:
    if list_val in list2:
        final_val.append(list_val)
        list2.remove(list_val)
print(final_val)












l1=[1,2,3,2,1]
l2=[2,2,1]
























# 513497 reverse given integer without using any string operation

num1=123
op=794315
reverse=0
temp=num1
while temp!=0:
    reverse=(reverse*10)+(temp%10)
    temp=temp//10
#
print(reverse)
# # print(num1)
# # print(type(num1))
# final_str=''
# for str_val in str:
#     final_str+=[final_str[::-1]]
#     break




















# l=[1,2,3]
# t=(1,2)
# Neha Nijampurkar3:10 PM
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# num1val=[1,2,2,1]
# def intersect_func(num1,num2):
#     final_val=[]
#     emp=[]
#     s=''
#     for listv in num1:
#         if listv in num2:
#              final_val.append(listv)
#              num2.remove(listv)
#              # s+=str(listv)
#              # emp.append(listv)
# #     # for num1_val in num1:
# #     #     for num2_val in num2:
# #     #         if num2_val==num1_val :
#     #             final_val.append(num1_val)
#     return s,emp,final_val
#
# print(intersect_func([1,2,2,1,],[2,2,1,1]))
# num1_val=[1,2,2,1]
# nums2_val = [2,2]
# print(set(num1_val).intersection(nums2_val))

# s = 'PythonDeveloperAndJavaDeveloper'
# op = 'python_developer'
# final_str=''  #P_ythonD_eveloper
# for str_val in s:
#     if s[0]==str_val:
#         final_str=final_str+str_val.lower()
#         continue
#     elif str_val==str_val.upper():
#         final_str=final_str+'_'+ str_val.lower()
#         continue
#     else:
#         final_str+=str_val
# print(final_str)
"""l = [{'price': 101, 'barcode': '2342355', 'dt': '31-08-2020'},
     {'price': 88, 'barcode': '2345566', 'dt': '31-08-2019'},
     {'price': 100, 'barcode': '2345577', 'dt': '30-11-2019'}]
i, j = '01-01-2019', '31-12-2019"""
l = [{'price': 101, 'barcode': '2346677', 'dt': '31-08-2020'},
     {'price': 88, 'barcode': '2345566', 'dt': '31-08-2019'},
     {'price': 100, 'barcode': '2345577', 'dt': '30-11-2019'},
     {'price': 101, 'barcode': '2345577', 'dt': '30-11-2019'}]

i='01-01-2019'
j='31-12-2019'
i1=j[6:]
j1=i[6:]
count=0
max_val=[]
for list_val in l:
    dste=list_val.get('dt')
    if count<=int(list_val.get('barcode')) and j1==dste[6:] and i1==dste[6:]:
        count=int(list_val.get('barcode'))
        max_val.append(('Price is ',list_val.get('price'),'Barcode is',list_val.get('barcode')))
print(max_val[-1])

# user id name city age
# user.objects.all().order_by("-age")[0:] & user.objects.filter(city_starwith="pune")


# >>> qs=Employee.objects.all().order_by("-salary")[0:] & Employee.objects.filter(name__startswith="suresh")



