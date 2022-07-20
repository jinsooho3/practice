list1 = [3,4,5]
list2 = [8,9,19]

#merged_list = list1 + list2

list1.extend(list2)

for value in list1:
    print(value)