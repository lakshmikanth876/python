list1=[1,2,3,4,5,6]
list2=[7,8,9]
print(list1 + list2)
list1.extend(list2)
print(list1)
print(list2)
for i in list1:
    print(i)
print(list1[-1])
print(list2[-2])