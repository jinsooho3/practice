from functools import total_ordering
import random

randList = []
maxnum = 0
minnum = 20
sumcount = 0
avrgnum = 0
# 1~20사이 양의 정수 중 난수 값 20개 생성후 리스트에 저장
for a in range(20):
    randList.append(random.randint(1,20))
print("랜덤 값 : ")
#리스트 출력
for indexNum in range(len(randList)):
    if indexNum ==10:
        print("\n")
    print(randList[indexNum]," ",end="")
print()
# 원소 값에 대한 최소값 최대값 합계 평균 출력

#최소값
for count in range(len(randList)):
    
    if randList[count] < minnum:
        minnum = randList[count]
print("최소값은 : ",minnum)

#최대값
for count in range(len(randList)):
    if randList[count] > maxnum:
        maxnum = randList[count]
print("최대값은 : ",maxnum)

#합계
for count in range(len(randList)):
    sumcount += randList[count]
print("합계\t: ",sumcount)

#평균
avrgnum = sumcount/ len(randList)
print("평균\t: ",avrgnum)

#list 내 중복 값과 중복 횟수 정보 출력
print("중복값\t중복 회수")
#중복을 제외한 리스트작성
onelist = []
for z in range(len(randList)):
    if randList[z] in onelist:
        continue
    else:
        onelist.append(randList[z])
#중복제외리스트 순서대로 나열

for cd in range(len(onelist)):
    chgnum=0
    for de in range(cd+1, len(onelist)):
        if onelist[cd] > onelist[de]:
            chgnum = onelist[cd]
            onelist[cd]=onelist[de]
            onelist[de]=chgnum

    
#중복없는 리스트에서 랜덤리스트에 하나씩 비교하면서
for ab in range(len(onelist)):
    samecount = 0
    for bc in range(len(randList)):
        #값이 같을경우 카운트 증가
        if onelist[ab] == randList[bc]:
            samecount +=1
    #숫자가 하나만 나온경우에는 패스
    if samecount == 1:
        continue
    #2개이상나온경우 원소와 중복횟수 출력
    else:
        print(" ",onelist[ab],"\t   ",samecount)

#구간 별 히스토그램 정보 출력
tofive=0
toten=0
tofift=0
totwen=0
for a in range(len(randList)):
    if 1<=randList[a]<=5:
        tofive +=1

    elif 6<=randList[a]<=10:
        toten +=1

    elif 11<=randList[a]<=15:
        tofift +=1
    else:
        totwen+=1
print("1 ~ 5 : ","*"*tofive)
print("6 ~ 10 : ","*"*toten)
print("11 ~ 15 : ","*"*tofift)
print("16 ~ 20 : ","*"*totwen)
