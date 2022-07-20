# 1~20 사이 양의 정수 중 난수 값 20개 생성 후  List에 저장
import random

alist = []
print("랜덤 값")
for a in range(20):
    alist.append(random.randint(1,20))
    #랜덤값 출력
    if a % 10 == 0 and a//10 >=1:
        print("\n")
    print(alist[a]," ",end='')
print()
#list 내 원소 값에 대한 최소값, 최대값, 합계, 평균 출력

#최소값
minnum = 20
for a in range(len(alist)):
    if minnum > alist[a]:
        minnum = alist[a]
print("최소 값 :",minnum)

#최대값
maxnum = 0
for a in range(len(alist)):
    if maxnum < alist[a]:
        maxnum = alist[a]
print("최대 값 :",maxnum)

#합계
sumcount = 0
for a in range(len(alist)):
    sumcount += alist[a]
print("합계\t:",sumcount)

#평균
print("평균\t:",sumcount/20)

#list 내 중복 값과 중복 횟수 정보 출력
print("중복 값\t중복 회수")
#중복값을 넣을 리스트 생성
blist=[]
for a in range(1,21):
    if a in alist:
        blist.append(a)

#blist에서 alist랑 비교하면서 몇번카운트되는지
#2번 이상이 아니라면 중복으로 나온게 아니므로
#취급하지 않는다

for a in range(len(blist)):
    samecount = 0
    for b in range(len(alist)):
        if blist[a] == alist[b]:
            samecount += 1
    if samecount >=2:
        print(" ",blist[a],"\t  ",samecount)
    
#구간별 히스토그램
five = 0
ten = 0
fift = 0
twen = 0
print("구간별 히스토그램")
#alist원소들이 어느 구간에있는지 조건을 달아서
#구간별로 카운트 증가
for a in range(len(alist)):
    if 1<=alist[a]<=5:
        five +=1
    elif 6<=alist[a]<=10:
        ten +=1
    elif 11<=alist[a]<=15:
        fift+=1
    elif 16<=alist[a]<=20:
        twen +=1
print(" 1~  5 :","*"*five)
print(" 6~ 10 :","*"*ten)
print("11~ 15 :","*"*fift)
print("16~ 20 :","*"*twen)