import random

#0~9사이 중복되지 않은 양의 정수 3개 생성
baseball= []
while len(baseball)<3:
    num = random.randint(0,9)
    if num not in baseball:
        baseball.append(num)

strikeOut = 0 #삼진 횟수
trycount = 1 

#게임 시작
while True:
    #사용자로부터 양의 정수 3개 입력
    playlist =[]
    strike = 0
    ball = 0

    for a in range(3):
        while True:
            num = int(input(str(a+1)+"번째 정수를 입력하세요"))
            if num not in playlist:
                playlist.append(num)
                break
    #스트라이크 볼 판정
    for a in range(3):
        if playlist[a]==baseball[a]:
            #스트라이크
            strike += 1
        elif playlist[a] in baseball:
            #볼
            ball += 1
    #삼진 또는 볼 +스트라이크 현황 출력
    if strike ==0 and ball == 0:
        #삼진
        strikeOut +=1
        print("삼진, ",strikeOut,"회")
    else:
        print("Strike: ",strike,"Ball : ",ball)
    #종료

    #다맞았을경우
    if strike >=3:
        print("클리어, 종료")
        break
    #삼진
    if strikeOut >=2:
        print("삼진2회, 종료")
        break
    #게임 시도 횟수 5번이상
    if trycount >=4:
        print("게임회수 5이상, 종료")
        break
    