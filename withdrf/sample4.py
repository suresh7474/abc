
unsequence=[0,9,3,8,2,7,0]
def quick_sort(sequnce):
    lseq=len(sequnce)
    if lseq <=1:
        return sequnce
    else:
        piovt=sequnce.pop()

    greater_item=[]
    lessthan=[]
    for item in sequnce:
        if item >= piovt:
            greater_item.append(item)
        else:
            lessthan.append(item)

    return quick_sort(lessthan)+[piovt]+quick_sort(greater_item)

print(quick_sort(unsequence))






















# a='Hellow wordo'
# final_val=''
# for str_val in a:
#     if str_val=='o':
#         final_val+='@'
#         continue
#     final_val+=str_val
# print(final_val)

# b='10111010101000000101010101011000010'
# c=0
# d=''
# p=0
# emp=[]
# for i in b:
#     if i=='0':
#         c+=1
#         d+='1'
#     else:
#         d+='0'
#         p=c
#         emp.append(p)
#         c=0
# print(max(emp))
# a=[]
# l=[2,6,310,8,]
# counts1=0
# counts2=0


# a=[10,20,30,40]
# b=[11,22,33,44]
# a_len=len(a)
# b_len=len(b)
# i1,j1=0,0
#
# emp12=[]
# for a1 in range((len(a)*2)-1):
#     if a[i1]<=b[j1]:
#         emp12.append(a[i1])
#         i1+=1
#     else:
#         emp12.append(b[j1])
#         j1+=1
# print(emp12)

# a=[]
# l=[1,2,310,4]
# counts1=1
# for j in  range(len(l)):
#     minval=j
#     for i in range(j+1,len(l)):
#         if l[i]<l[minval]:
#             minval=i
#     if j!=minval:
#         l[j], l[minval] = l[minval], l[j]
# print(l)
            # counts1=i
#     a.append(counts1)
#     l.remove(counts1)
#     counts1=0
# print(a[0])

# for j in range(5):
# for i in l:
#    if i>=counts1:
#         counts1=i
#         a.append(counts1)
#
# print(counts1)
# print(counts1)


# print(max(emp))
# print(d)
# print(max(emp))














# print(a.replace('o','0'))
# for c,i in enumerate(a):
#     if i=='o':
#         b+='0'
#     elif i!='o':
#         b+=i
# print(b)
#
