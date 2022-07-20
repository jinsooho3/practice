import random
#0~9사이 정수 중 중복값없는 난수 3개 생성
baseball = []
while len(baseball)<3:
    randnum = random.randint(0,9)
    if randnum not in baseball:
        baseball.append(randnum)

strikeOut = 0
countNum =0

while True:

    countNum +=1
    if countNum >=5:
        print("게임횟수 초과")
        print("졌습니다")
        print("정답은:",baseball,"입니다")
        break

    playlist = []
    #키보드로 0~9사이 정수 3개입력받고 결과값 출력
    print("시도횟수:",countNum)
    print("정수 3개를 입력하세요")
    for a in range(len(baseball)):
        playlist.append(int(input()))
    print(playlist)

    strike= 0
    ball = 0
    out = 0
    #strike ball out 판별
    for a in range(len(baseball)):
        if playlist[a] in baseball:
            if playlist[a] == baseball[a]:
                strike +=1
            else:
                ball +=1
        else:
            out +=1

    #판별후 결과 출력
    if out == len(baseball):
        strikeOut +=1
        if strikeOut ==2:
            print("아웃횟수 초과")
            print("패배~ 정답은:",baseball,"였습니다")
            break
        else:
            print("Out: 아웃",strikeOut,"번")

    if strike>0:
        if strike ==len(baseball):
            print("승리~~")
            print("정답은:",baseball,"였습니다")
            break
        else:
            print(strike," Strike")
    if ball >0:
        print(ball," Ball") 