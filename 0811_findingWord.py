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
    if 3 < len(inputWord) < 20 and inputWord not in wordList:
        wordList.append(inputWord)
    else:
        print("다시 입력해주세요")   

# 50%이상을 _ 로 출력하기
randomWord = random.choice(wordList)
underBarNum = []
while len(underBarNum) < banUp(len(randomWord)):
    randNum = random.randint(0, len(randomWord))
    if randNum not in underBarNum:
        underBarNum.append(randNum)

while True:
    for index in range(len(randomWord)):
        if index in underBarNum:
            print("_", end = '')
        else:
            print(randomWord[index], end = '')
    print()
    inputChar = input("알파벳 입력하세요 :")
    for count in underBarNum:
        if randomWord[count] == inputChar:
            underBarNum.remove(count)
    if len(underBarNum) == 0:
        print(randomWord)
        break