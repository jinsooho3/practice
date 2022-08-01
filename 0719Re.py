import random

N = 5
NoE = N * N
randfrom = 1
randto = 50
randNumList = [46, 43, 47, 1, 17, 42, 41, 38, 9, 12, 34, 40, 25, 20, 24, 49, 30, 27, 36, 28, 32, 3, 8, 5, 4]
# while len(randNumList) < NoE:
#     num = random.randint(randfrom, randto)

#     if num not in randNumList:
#         randNumList.append(num)

for index in range(NoE):
    print(randNumList[index], "\t",end='')
    if (index + 1) % 5 == 0:
        print()

for col in range(N):
    tempList = []
    for row in range(N):
        tempList.append(randNumList[row*N + col])
    
    tempList.sort()

    print(tempList[0],tempList[-1],tempList[N//2])

print()
for col in range(N):
    tempList = []
    for row in range(N):
        tempList.append(randNumList[col*N + row])
    
    tempList.sort()

    print(tempList[0],tempList[-1],tempList[N//2])

randNumList.sort()
print()
print(randNumList[0],randNumList[-1],randNumList[len(randNumList)//2])