"""Challenge
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above."""



def consecutive_zeros(strval):
    a = 0
    b=[]
    for item in strval:
        if int(item)==0:
            a+=1
        else:
            b.append(a)
            a=0
    print(max(b))
        # if int(item)==0:
        #     b.append(a)
        #     a=0
    # print(b)
            # print(item)
    print(a)
consecutive_zeros("1001101000110")






# class A:
#     def m1(self):
#         print('This is class A')
#
# class B(A):
#     print("This is class B")
#
# class C(B):
#     print("This is Class ")
#
# a=C()
# a.m1()#
#
# name,add ---pune
# qs=Stdent.objects.filter(add_strtwith='pune')
# print(qs)





import sys
sys.exit(0)

# class Geeks:
#     def __init__(self):
#         self._age = 0
#
#     # using property decorator
#     # a getter function
#     # @property
#     def get(self):
#         print("getter method called")
#         return self._age
#
#     # a setter function
#     # @age.setter
#     def set(self, a):
#         if (a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#         print("setter method called")
#         self._age = a
#
#     age=property(get,set)
# mark = Geeks()
#
# mark.age = 20
#
# print(mark.age)



class Person:
    def __init__(self):
        self._age=0

    def get(self):
        return self._age

    def set(self, a):

        if (a < 18):
                raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a

    # def set(self,a):
    #     if a<18:
    #         raise ValueError('You are not eligible in the exam')
    #     print('setter method')
    #     self._age=a
    age1=property(get,set)

# print(Person()._age)
o=Person()
o.age=17
print(o.age)




# from abc import ABC,abstractmethod
#
# class Computer(ABC):
#     @abstractmethod
#     def processor(self):
#         print('......................')
#
# c=Computer()
# class Laptop:
#     def memory(self):
#         print('This is memory class')
#
# class Dekstop(Laptop):pass
#         # def processor(self):
#         #     print('This is abstrac class')
#
# lclass Developer:
#     def work(self,com):
#         print('To solve bug')
#         com.processor()
#
# import  unittest
# class Testlaptop(unittest.TestCase):
#     def setUp(self):
#         self.l1=Developer()
#         self.l2=self.l1
#     def test_laptopinstance(self):
#         return  self.assertEqual(self.l1,self.l2)
# if __name__ == '__main__':
#     unittest.main()








# d1=Dekstop()
# l.processor()
# d=Developer()
# d.work(d1)










# a=[1,2,1,3,4,1,243,4,2]
# final_list=[]
# for item in a:
#     if item not in final_list:
#         final_list.append(item)
#
#     else:
#         final_list.remove(item)
#
# print(final_list)#Time complexity is O(n)