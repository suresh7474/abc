# num=12
# str_val=str(num)
# revese=str_val[::-1]
# intrevese=int(revese)
#
# if num==intrevese:
#     print("This is palandrom")
# else:print("This is not palendrom")

def palandrom(num):
    tem=num
    revesr=0

    while tem != 0:
        revesr=(revesr*10) + (tem%10)
        tem=tem//10

    if revesr==num:
        print(num, " Is palandrom")
    # else:
    #     print(num,"Is not palandrom")
# count=10
# while count<200:
#     palandrom(count)
#     count+=1
# print(l.remove(9))#
# print(l.pop(0))#
# l=[1,2,3]
# print(l.remove(2))
# print(l.pop(3))



# num=11
# tem=num
# rever=0
#
# while tem!=0:
#     rever= (tem* 10)+ (tem%10)
#     tem=tem//10
#
# if num==rever:
#     print('This is palendrome')
# else:print("This is not palendrome")



















# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return True
#     else:
#         return False
#
#
# pal=is_palindrome(12)
# print((pal))




# class custom:
#     def __init__(self):
#         self.max=0
#     def __iter__(self):
#         self.cout=0
#         return self
#     def __next__(self):
#         self.cout+=3
#         return self.cout
#
# c=custom()
# a=iter(c)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(c))










# arr=[1,2,2,3,4,5]
# counts=0
# counts1=''
# sort=sorted(arr)
# for index,value in enumerate(arr):
#     if counts < value:
#         counts=value
#         counts1+=str(value)
#
#
# if arr == sort:
#     print('This is countinous list')
# else:print("This list is not continous")


# count=0
# str_val=''
# c=''
#
# for item in range(len(arr)):
#     if count < arr[item] :
#         count+=1
#         str_val+=str(arr[item])
#
# if len(arr)==len(str_val):
#     print('This list is continous ')
# else: print("This list is not continous")


   # emp id name salary
    # select id from emp order_by desc salary
    # emp.objects.filter.oreder_by("-salary")[2] & emp.objects.all().only('id')
# def gen_fun(n):
#     for item in range(n):
#         yield item
#     # yield 2
#     # yield 3
# g=gen_fun(10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

    # if item > count:
    #     count=item
    #     print(index)
    # elif item < count:
    #     print("This  list is not continous")
    #     break
    #
    # elif len(arr)-1==index:
    #     print("This list is continous")
    # else:
    #     pass


#     try:
#         if item - arr[index]==-1:
#             strval.append(arr[index]+arr[index+1])
#             print('This list ')
#     except IndexError:
#         print('pass')
# print(strval)






























# str_="11100011100000111"
# count=0
# b=0
# emp_list=[]
# for item in str_:
#     if item=='0':
#         count+=1
#     else:
#         b=count
#         emp_list.append(count)
#         count=0
# print(max(emp_list))



# emplist=[]
# emplist.append('a')
# emplist.append('b')
# emplist.append('c')
# print(emplist)
# print(emplist.pop())
# print(emplist.pop())
# print(emplist.pop())
# for item in emplist:
#     print(item)
# import  more




