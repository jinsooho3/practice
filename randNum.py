import random

answerNum = random.randint(1,20)
lifeNum = 4
for count in range(lifeNum):
    chNum= int(input("기회가{}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요 :".format(lifeNum-count)))
    if chNum < answerNum:
        print("Up")
    elif chNum > answerNum:
        print("Down")
    elif chNum == answerNum:
        print("축하합니다. ",count+1,"번만에 숫자를 맞히셨습니다.")
        break
if chNum != answerNum:
    print("아쉽습니다. 정답은",answerNum,"입니다")