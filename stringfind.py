#사용자로부터 입력받을 문자열의 라인수 입력
line = int(input("입력 문자열의 줄(Line) 수를 입력하세요"))

inputText = []
for value in range(line):
    #문자열 입력받고 리스트에 저장
    print(value+1,end='')
    inputText.append(input("번째 라인의 문자열을 입력하세요."))
#검색할 단어 유 무 출력
searchedLine = []       #찾을려는 단어가 어느줄에 있는지 저장할 리스트


while True:
    wordCount = line
    searchCount = 0
    search = input("검색 할 문자열을 입력하세요.")
    #단어가 있으면 어느줄에있는지
    for value in range(len(inputText)):
        if search in inputText[value]:
            searchedLine.append(value+1)

        
        for a in range(len(inputText[value])):
            #띄어쓰기 있을때마다 단어 횟수 추가
            if inputText[value][a] == " ":
                wordCount +=1

    if searchedLine == []:
        print("찾을 수가 없습니다.",end='')
        continue
    else:
        break
print("검색된 라인 수 : ",searchedLine)
print("검색된 횟수 : ")
print("총 단어 수 : ",wordCount)