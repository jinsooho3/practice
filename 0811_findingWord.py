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
randomWord = random.choice(wordList)
underBarNum = []
while len(underBarNum) < banUp(len(randomWord)):
    randNum = random.randint(0, len(randomWord) - 1)
    if randNum not in underBarNum:
        underBarNum.append(randNum)

tryCount = 0
while True:
    tryCount += 1

    print(tryCount,"번째 시도, 아래단어를 구성하는 알파벳 한개를 입력하세요.")

    for index in range(len(randomWord)):
        if index in underBarNum:
            print("_", end = '')
        else:
            print(randomWord[index], end = '')
    print()
    correctChar = []
    
    inputChar = input()
    if inputChar in randomWord:
        for count in underBarNum:
            if randomWord[count] == inputChar:
                correctChar.append(count)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")

    
    for index in correctChar:
        underBarNum.remove(index)

    if len(underBarNum) == 0:
        print("Clear - 선택된 단어 : ",randomWord,", 총 시도 횟수 : ",tryCount)
        break