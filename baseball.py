import random

#중복값없는 난수 생성
baseball = []
while len(baseball)<3:
    randnum= random.randint(0,9)
    #중복이 나올경우 다시 난수생성
    if randnum in baseball:
        continue
    baseball.append(randnum)

life =1
outcount =0
while True:
#키보드로 정수입력받고 결과값출력
    playlist=[]
    print("실행 횟수:",life)
    print("정수 3개를 입력하세요")
    for a in range(3):
        playlist.append(int(input("")))
    print(playlist)
    print()

#스트라이크,볼판정
    strike = 0
    ball = 0
    out = 0
    for a in range(len(playlist)):
        #입력받은 항목이 랜덤리스트에 있으면
        if playlist[a] in baseball:
            #입력받은항목이 리스트에있고 자리도 같으면
            if playlist[a] == baseball[a]:
                strike +=1
            #리스트에있지만 자리가 다르면
            else:
                ball +=1
        #입력받은 항목이 리스트에 없으면
        else:
            out +=1
    #스트라이크 볼 아웃 출력
    if out ==3:
        outcount +=1
        #2아웃일경우 게임오버
        if outcount ==2:
            print("아웃횟수 초과")
            print("패배! 정답은 :{}였습니다".format(baseball))
            break
        print("Out: 아웃", outcount,"번")
    
    if strike >0:
        #3 strike일 경우 승리
        if strike == 3:
            print("승리!",life,"번만에 정답을 맞췄습니다")
            print("정답은 :",baseball,"입니다")
            break
        print(strike," Strike")
    if ball > 0:
        print(ball," Ball")
    print()
    life +=1
    #시도횟수 초과시 게임오버
    if life >=5:
        print("실행 횟수 초과")
        print("정답은 :",baseball,"였습니다")
        break