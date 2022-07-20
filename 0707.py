myList = [5, 10, 15, 20,5]

for value in myList:
    print(value)


# del
#del myList[2]

# remove
# 0번째부터 ()안의 원소를 찾고 찾으면 삭제후 끝
myList.remove(5)


print("-"*10)
for value in myList:
    print(value)
