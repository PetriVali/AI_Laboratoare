def sum_lists(list1, list2):
    for i, (list1_item, list2_item) in enumerate(zip(list1, list2)):
        yield list1_item + list2_item


list1 = [1, 2, 3,4,5]
list2 = [10, 20, 30,40,50]
result = sum_lists(list1, list2)
print(list(result))
