import random
#난수 리스트 생성
totalList = []
N = 5
while len(totalList)< N * N:    # 1~50 사이의 정수에서 난수 25개를 골라 리스트에 저장
    randNum = random.randint(1,50)
    if randNum not in totalList:
        totalList.append(randNum)
for count in range(len(totalList)):
    if count % 5 == 0:
        print()
    print(totalList[count]," ",end='')

print()
for col in range(N):
    templist = []
    for row in range(N):
        templist.append(totalList[row*N+col])
        templist.sort()
    print(templist[0],templist[-1],templist[len(templist)//2])

for row in range(N):
    templist = []
    for col in range(N):
        templist.append(totalList[col*N+row])
        templist.sort()
    print(templist[0],templist[-1],templist[len(templist)//2])

totalList.sort()
print(totalList[0],totalList[-1],totalList[len(totalList)//2])