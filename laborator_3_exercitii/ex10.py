
list1 = [i+1 for i in range(100)]
print(list1)
list2 = [i*i*i for i in range(10) ]
print(list2)
list3 = [x for x in list1 if x in list2]
print(list3)
