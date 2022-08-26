import random
# 함수 정의
def banUp(argA):
    argA = argA / 2
    if argA - int(argA) < 0.5:
        return int(argA)
    else:
        return int(argA) + 1

# 단어 3개를 입력받음
# ※단 단어의 길이가 3글자이하, 20글자를 넘어가면 재입력
wordList = []

while len(wordList) < 3:
    print(len(wordList) + 1, end = '')
    inputWord = input("번째 단어를 입력해주세요")
    if 5 <= len(inputWord) <= 20 and inputWord not in wordList:
        wordList.append(inputWord)
    else:
        print("다시 입력해주세요")   

# 50%이상을 _ 로 출력하기

# 단어길이만큼에서 랜덤으로 (50%) _ 로 표시할 부분을 선택
randomWord = random.choice(wordList)
underBarNum = []
while len(underBarNum) < banUp(len(randomWord)):
    randNum = random.randint(0, len(randomWord) - 1)
    if randNum not in underBarNum:
        underBarNum.append(randNum)

tryCount = 0        #시도횟수
while True:
    tryCount += 1   #시도할때마다 1추가해서 몇번째 시도인지 확인

    print(tryCount,"번째 시도, 아래단어를 구성하는 알파벳 한개를 입력하세요.")

    # 위에서 언더바로 표시할곳에서는 언더바로 출력 나머지는 그대로 영어표시
    for index in range(len(randomWord)):
        if index in underBarNum:
            print("_", end = '')
        else:
            print(randomWord[index], end = '')
    print()

    # 알파벳 입력받고 일치하는 알파벳이 있으면 correctChar리스트에 추가 없으면 아래문장 출력
    correctChar = []
    inputChar = input()
    if inputChar in randomWord:
        for count in underBarNum:
            if randomWord[count] == inputChar:
                correctChar.append(count)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")

    # 일치하는 알파벳이있으면 그부분을 언더바로 출력하는 리스트에서 삭제
    for index in correctChar:
        underBarNum.remove(index)

    # 언더바리스트에 원소가 없으면(다 맞추면) 게임종료
    if len(underBarNum) == 0:
        print("Clear - 선택된 단어 : ",randomWord,", 총 시도 횟수 : ",tryCount)
        break