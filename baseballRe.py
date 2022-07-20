import random
#게임 시작시 0~9사이 정수중 중복없이 난수3개생성
baseball = []
while len(baseball)<3:
    randNum = random.randint(0,9)
    if randNum not in baseball:
        baseball.append(randNum)
outcount =0
countNum = 1
#키보드로부터 0~9사이 정수 3개입력받고 결과값 출력
while True:
    print("시도횟수:",countNum)
    playlist = []
    print("정수 3개를 입력하세요")
    for a in range(len(baseball)):
        playlist.append(int(input()))
    print(playlist)
    #strike ball 판별
    strike =0
    ball = 0
    out = 0
    for a in range(len(playlist)):
        if playlist[a] in baseball:
            if playlist[a] == baseball[a]:
                strike +=1
            else:
                ball +=1
        else:
            out+=1
    #결과 출력
    if out ==3:
        outcount +=1
        #Strike out ==2일시 게임Lose
        if outcount ==2:
            print("아웃횟수 초과")
            print("패배~ 정답은 :",baseball,"였습니다")
            break
        else:
            print("Out: 아웃",outcount,"번")
    if strike>0:
        if strike==3:
            print("승리~ 정답은",baseball,"이 맞습니다")
            print(countNum,"번만에 정답을 맞췄습니다")
            break
        else:
            print(strike," Strike")
    if ball>0:
        print(ball," Ball")
    #시도횟수 >=5 일시 게임 Lose
    countNum +=1
    if countNum >=5:
        print("게임횟수 초과")
        print("정답은:",baseball,"였습니다")
        break