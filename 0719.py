import random
#sorting 직접 함수만들기~~ 

def mysort (a):     #직접만든함수
    for value in range(len(a)):
        chgnum = 0
        for num in range(value + 1, len(a)):
            if a[value] > a[num]:
                chgnum = a[value]
                a[value] = a[num]
                a[num] = chgnum

def mysort2 (a):    #bubble sorting 참고
    for start in range(len(a)-1):
        for value in range(len(a) - start - 1):
            if a[value] > a[value + 1]:
                a[value] , a[value + 1] = a[value + 1], a[value]

# 1~ 50까지의 정수 25개 난수로 리스트에 추가
matrixList = []             #전체 리스트
while len(matrixList) < 25:
    randnum = random.randint(1,50)
    if randnum not in matrixList:
        matrixList.append(randnum)
#리스트 출력
valueList = [] #행 리스트
cutlist = []        
for a in range(len(matrixList)):
    cutlist.append(matrixList[a])
    print(matrixList[a], " ", end='')   
    if a % 5 == 4:                      
        print("\n")
        valueList.append(cutlist)
        cutlist = []

colList = []  #열 리스트
for a in range(5):
    for b in range(5):
        cutlist.append(valueList[b][a])
    colList.append(cutlist)
    cutlist = []

for a in colList:
    mysort(a)
#열 최소값,최대값,중간값 출력
print("열")
print("최소값 : ",end='')
for a in range(len(colList)):
    print(colList[a][0]," ",end = '')
print("\n")
print("최대값 : ",end = "")
for a in range(len(colList)):
    print(colList[a][len(colList)-1]," ",end='')
print("\n")
print("중간값 : ",end = "")
for a in range(len(colList)):
    print(colList[a][len(colList)//2]," ",end='')

#행 최소 최대 중간 값 출력
for a in valueList:
    mysort(a)
print("\n\n행")
print("최소값  최대값  중간값")
for a in range(len(valueList)):
    print(valueList[a][0],"\t" ,valueList[a][len(valueList)-1],"\t"  ,valueList[a][len(valueList)//2])

mysort(matrixList)

print("\n전체")
print("최소값 : ",matrixList[0])
print("최대값 : ",matrixList[len(matrixList)-1])
print("중간값 : ",matrixList[len(matrixList)//2])