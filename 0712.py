import random
baseball = []
while len(baseball)<3:
    randNum=random.randint(0,9)
    if randNum in baseball:
        continue
    baseball.append(randNum)
life=1
outcount =0
while True:
    print("시도횟수: ",life)
    playball = []
    print("정수 3개를 입력하세요")
    while len(playball)<3:
        playball.append(int(input("")))
    print(playball)
    strike = 0
    ball = 0
    out = 0 
    for a in range(3):
        if playball[a] in baseball:
            if playball[a] == baseball[a]:
                strike +=1
            else:
                ball +=1
        else:
            out +=1
    if strike ==3:
        print("승리! 정답은 ",baseball,"입니다")
        break
    if out ==3:
        outcount +=1
        if outcount ==2:
            print("아웃횟수 초과")
            print("정답은 ",baseball,"입니다")
            break
        print("Out: 아웃",outcount,"번")
    if strike >0:
        print(strike," Strike")
    if ball>0:
        print(ball," Ball")
    life +=1
    if life >4:
        print("게임횟수 초과")
        print("정답은: ",baseball,"입니다")
        break