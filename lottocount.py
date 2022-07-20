import random
count=0
lot_grade = 0
alist=[]
for lottonum in range(6):
    a = random.randint(1,45)
#중복번호가 나올경우 다시 난수 입력받기
    while a in alist:
        a = random.randint(1,45)
#리스트에 난수 넣기
    alist.append(a)
countsum = 0
for a in range(1000000):
    while lot_grade <6:             #숫자이상 중복된 숫자가 나오면 종료
        lot_grade=0
        play_list =[]
        while len(play_list)<6:
            randnum= random.randint(1,45)
            while randnum not in play_list:  
                play_list.append(randnum)

        for a in play_list:
            if a in alist:
                lot_grade += 1
        count+=1
    countsum += count
alist.sort()
play_list.sort()
print(alist)
print(play_list)
print(countsum/1000000)