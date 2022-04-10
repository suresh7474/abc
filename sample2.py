class A:
    print('This is parent class')
    def func(self):
        print("This is function of A")

class B(A):
    print('This is class B')
    def func(self):
        print("This is function of A")

class C(B):
    print('This is class C ')


# c=C()
# b=B()
# b=B()
# b.func()
# c=C()
# c.func()
arr=[1,1,2,2,3,4]


# l={1,1,2,2,3,4}.union({1,1,2,2,3,4})
# print(l)
# emp_list=[]
# for i in s:
#     print(arr.remove(i))
# print(arr)
#     if i  not in emp_list:
#         emp_list.append(i)
#     else:
#         print(i)
#
# print(emp_list)


# a=0
# for i in range(len(arr)):
#     arr.count(i)
# a={1,2,3,1}
# b={1,2,1}
# c=a.intersection(b)
# print(c)
# for item_val in arr:
#     if arr.count(item_val)<2:
#         print(item_val)





# s1={1,1,2,2,3,4}
# s2={1,1,2,2,3,4}
# final_out=s2.intersection(s1)
# print(final_out)


import sys
sys.exit(0)





from abc import ABC,abstractmethod

class Employe(ABC):
    @abstractmethod
    def manager(self):
        pass







# name='suresh'
# email='Suresh@gmail.com'
# s1=f"name-{name},email-{email}"
# s2="name{name},age{email}".format(name=name,email=email)
# s3=name+email
# print(s2)

# SELECT id, name FROM users WHERE is_staff=True ORDER BY id DESC LIMIT 10;
# qs=User.objects.all().values(id,name)
# qs1=User.objects.filter()
import sys
sys.exit(0)
import  unittest
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

class My_test(unittest.TestCase):
    def setUp(self):
        print('setup fuction call')
        self.a=10
        self.b=20
    def test_fun1(self):
        print('fun1............')
        result=mul(self.a,self.b)
        return self.assertEqual(result,self.a*self.b)

    def test_fun2(self):
        print('func2 .............')
        result=add(self.b,self.a)
        return self.assertEqual(result,self.a+self.b)

    def tearDown(self):
        print('TearDown function call')

if __name__ == '__main__':
    unittest.main()









import sys
sys.exit(0)
# x
# print(list(map(lambda_fun,l1)))
class Employee_info():
    def __init__(self,name,email,adr):
        self.name=name
        self.email=email
        self.address=adr
    def __str__(self):
        return (f'name -{self.name}, email{self.email}, address-{self.address}')
    # @abstractmethod
    def salary(self,basic):
        # pass
       print("salary present in  Employee_info")
class Manager(Employee_info):
    pass
class Hr(Employee_info):
    def __init__(self,name,email,adr):
        super().__init__(name,email,adr)
    def salary(self,basic):
        super().salary(basic)

objHr=Hr('Rahul',"R@gmail.com",'Pune')
print(objHr)
objHr.salary(400)
from  abc import ABC,abstractmethod

import sys
sys.exit(0)
from abc import ABC,abstractmethod

class Employee_info(ABC):
    def __init__(self,name,email,adr):
        self.name=name
        self.email=email
        self.address=adr
    def __str__(self):
        return (f'name -{self.name}, email{self.email}, address-{self.address}')
    @abstractmethod
    def salary(self,basic):
        pass
        # print("salary present in  Employee_info")

class Manager(Employee_info):
    pass

class Hr(Employee_info):
    def __init__(self,name,email,adr):
        super().__init__(name,email,adr)
    def salary(self,basic):
        super().salary(basic)

objHr=Hr('Rahul',"R@gmail.com",'Pune')
print(objHr)
# a=objHr('Rahul',"R@gmail.com",'Pune')
# objHr.salary(4000)
# print(objHr('Rahul',"R@gmail.com",'Pune'))

import sys
sys.exit(0)
def outer(func):
    def inner(a,b):
        if type(a)==int and type(b)==int:
            func(a,b)
        else:
            print('Please enter integer value')
    return inner

@outer
def mul(a,b):
    print(a*b)
    # return a*b
outer(mul(20,'30'))
# mul(10,20)
# print(m)
# print(outer(mul(10,20)))














# Sample
# code
# c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# c.encode('Codewars') # returns 'HTIJBFWX' HTIJ|FWT
# HTIJBFWX
# WAFFLES
# c.decode('BFKKQJX') # returns 'WAFFLES'
import sys
sys.exit(0)

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift=shift

    def encode(self, st):
        str_val = ''                    #empty string to get final value
        for shift_item in st.upper():   #convert all charachtor into Upper case
            if ord(shift_item)<86:      #chech char val less than < 86
                str_val+=chr(ord(shift_item)+self.shift).upper() #add..shift_item +self.shift and store in str_val
            else:
                a=ord(shift_item)+self.shift #shift_item is greater than >87 and add self.shift val
                b=a-90                       # f
                final_va1=chr(b+65-1)
                str_val+=final_va1
        print(str_val)

    def decode(self, st):
        for shift_item in st.upper():
            str_val = ''
            if ord(shift_item) >69:
                str_val += chr(ord(shift_item) - self.shift).upper()
            else:
                l=ord(shift_item)-self.shift
                l2=chr(90-(65-l)+1)
                str_val+=l2
            print(str_val, end='')

obj1=CaesarCipher(5)
obj1.encode('uCodewars')
# obj1.decode('BFKKQJX')

print(chr(85))










from functools import reduce











# l1=[1,2,3,4,5]
# lambada_func=lambda a,b:a+b
# print(list(map(lambada_func,l1)))
# print(reduce(lambada_func,l1))
import  sys
sys.exit(0)
from collections import deque
l1=[10,20,30]
deque_val=deque(l1)
deque_val.appendleft(0)
print(deque_val)

import copy
list1=[1,2]
a=copy.copy(list1)
a[0]=20
print(a)
print(list1)















# # class Process_values:
# #     def __init__(self):
# #         self.mydata=('1',2,'3','5')
# #
# #     def add_(self):
# #         for i in self.myvalue:
# #             print(i)
# #
# # a=Process_values
# # a.add_()
#
# import sys
# def num(fun):
#     def wrapper(*args,**kwargs):
#         val=fun(*args)
#         try:
#             return val+int(sys.argv[2])
#         finally:
#             return val+int(sys.argv[1])
#     return  wrapper
# @num
# def cal(a,b):
#     return a+b
# a=cal(7,8)
# print(a)
#
#
#
#
#
#
#
#
#
#
#
# # Key-value pair is nothin but dictionay
# # mutable,dict-key immutable
# # value-mutable
# # type methods
#
# # item()-
# # dict1={1:10,2:20,3:30}
# # for k,v in dict1.items():
# #     print('key -',k,'V-',v)
# # key - 1 V- 10
# # key - 2 V- 20
# # key - 3 V- 30
#
# # setdefault
# # key()
# # value()
# # Pop(K)
# # get(k)
# # update(k)
#
# # dict1={1:10,2:20,3:30}
# # a=tuple((dict1.items()))
# # print(a[2][0])
# # for k,v in dict1.items():
# #     print('key -',k,'V-',v)
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import re
#
# # s="gfdgfd976"
# # b={1:{'A':{"password":"suesh@123"}},"b":{10,20,30}}
# # print(b[1]["A"]["password"])
#
# # a=[1,2,3,[12,13,['suresh']]]
# # b=a.index('suresh')
# # print(a[3][2])
# # print(b)
#
# # s1=re.findall("[a-z]",s)
# # print(''.join(s1))
# # a=(''.join(s1))
# # print(a[-1])
# # for i in s.split():
# # a=re.finditer("\W",s)
# # for j in s.split():
# #     for i in a:
# #         if i.group()=='@':
# #             print(j,end=' ')
#         # print('\S+@\S+')
# # s1=re.findall('\S+@\S+',s)
# # print(s1)
# # print('          '.join(s1))
#
#
#
#
#
#
#
# # from abc import ABC,abstractmethod
# # class Employe(ABC):
# #     def __init__(self,name):
# #         self.name=name
# #
# #     @abstractmethod
# #     def adds(self,a,b):
# #         print(a+b)
# #
# # a=Employe('suresh')
# # a.adds(10,20)
# #
# #
