# l=[1,2,3]
# t=(1,2)
# Neha Nijampurkar3:10 PM
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersect_func(num1,num2):
    final_val=[]
    for num1_val in num1:
        for num2_val in num2:
            if num2_val==num2_val:
                final_val.append(final_val)
            # print(num1_val,num2_val)
        # if num1_val not in num2:
        #     final_val.append(num1_val)
        # else:print(num1)
    return final_val
print(intersect_func([1,2,2,1],[2,2]))


import sys
sys.exit(0)
















# class Employee:
#     def m1(self):
#         print('This is parent method')
#     def m2(self):
#         print("This is m2")
# class Manager(Employee):
#     print('This is child')
#     def m01(self):
#         print("this is m1 method of Child")
#
# ob=Manager()
# ob.m2()





# class should have only one responsibilty and not more
# class Book:
#     def __init__(self):
#         self.number=0
#         self.book={}
#
#     def add_book(self,bookname):
#         self.number+=1
#         self.book[self.number]=bookname
#
#     def __str__(self):
#         return str(self.book)
#
#     def save_book(self,filename):
#         with open(filename,'w') as f:
#             f.write(str(self.book))
#
# b=Book()
# b.add_book('python')
# b.add_book('java')
# b.save_book('c.tct')
# print(b)






















# SOLID principle - Class should have single responsibility not more
# class Book:
#     def __init__(self):
#         self.number=0
#         self.book={}
#
#     def add_book(self,bookname):
#         self.number+=1
#         self.book[self.number]=bookname
#
#     def __str__(self):
#         return str(self.book)
#
# class Save_booK():
#     @staticmethod
#     def save_book(filename,book):
#         with open(filename,"w") as f:
#             f.write(str(book))
#
# b=Book()
# b.add_book('Book A')
# b.add_book('Book B')
# s=Save_booK()
# s.save_book('b.txt',b)
# # print(f"{b}")

# s=[6,4,7,9,3,12]
# a=10
# for i in range(len(s)):
#     for j in range(len(s)):
#         for k in range(len(s)):
#             if i!=j!=k:
#                 if i+j+k==a:
#                     print(i,j,k)

# import re
#
# s = "abc"  # Example input
#
# # print(len(re.findall(r'^(\w*).*\1$', s)[0]))
#
# for i in range(len(s)//2,0,-1):
#     c1=s[0:i]
#     c2=s[len(s)-i:len(s)]
#     if c1==c2:
#         print(c1)
#     elif s.count(s[i])<=1:
#         print(s)
#



# s="ABABD"
#
#
# def longestPrefixSuffix(s):
#     n = len(s)
#     lps = [0] * n  # lps[0] is always 0
#
#     # length of the previous
#     # longest prefix suffix
#     l = 0
#
#     # the loop calculates lps[i]
#     # for i = 1 to n-1
#     i = 1
#     while (i < n):
#         if (s[i] == s[l]):
#             l = l + 1
#             lps[i] = l
#             i = i + 1
#
#         else:
#
#             # (pat[i] != pat[len])
#             # This is tricky. Consider
#             # the example. AAACAAAA
#             # and i = 7. The idea is
#             # similar to search step.
#             if (l != 0):
#                 l = lps[l - 1]
#
#                 # Also, note that we do
#                 # not increment i here
#
#             else:
#
#                 # if (len == 0)
#                 lps[i] = 0
#                 i = i + 1
#
#     res = lps[n - 1]
#
#     # Since we are looking for
#     # non overlapping parts.
#     if (res > n / 2):
#         return n // 2
#     else:
#         return res
#

# Driver program to test above function
# s = "abcab"
# print(longestPrefixSuffix(s))




# if no prefix and suffix match
    # occurs
    # return 0

# print(longestPrefixSuffix(s))
#





# longest prifix
# a="ABABD"
# m=(len(a)//2)
# print(a[0:m])
# print(a[len(a)-m:len(a)])
# print(a[0:len(a)//2])
# print(a[len(a)-len(a)//2:len(a)])
# print('hi')
# for i in range(m,0,-1):
    # print(i)
    # print(a[0:m])
    # print(a[len(a)-m:len(a)])
    # print(a[len(a)-i:len(a)])
#     print(a[len(a)-i:len(a)])
#     print('.....................')
#     if a[0:m]== a[len(a)-m:len(a)]:
#         print(a[i],i)
# m=len(a)//2
# print(a[0:m])
# print(a[len(a)-m:len(a)])

















# def outerfun(fun):
#     def innerfunc(str_val):
#         if type(str_val)== str:
#             print('33333333',str_val)
#             typecast=int(str_val)
#             return fun(typecast)
#     return innerfunc
# @outerfun
# def normalfuc(str_val1):
#     print(type(str_val1),str_val1)
#     return str_val1
#
# print(normalfuc('123'))


