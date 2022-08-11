# 단어 3개를 입력받음
# ※단 단어의 길이가 3글자이하, 20글자를 넘어가면 재입력
wordList = []
wordNum = 3
while len(wordList) < 3:
    print(len(wordList) + 1, end = '')
    inputWord = input("번째 단어를 입력해주세요")
    if 3 < len(inputWord) < 20 and inputWord not in wordList:
        wordList.append(inputWord)
    else:
        print("다시 입력해주세요")
print(wordList)