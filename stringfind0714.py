englishLine = []        #문자열 리스트 생성
searchedLine = []
searchedCount = 0
#몇줄의 영문 문자열을 입력받을것인지
line = int(input("입력 문자열의 줄(line) 수를 입력하세요"))
for value in range(line):
    print(value + 1, end = '')
    #영문 문자열을 키보드로 입력받고 문자열 리스트에 추가
    englishLine.append(input(" 번째 라인의 문자열을 입력하세요."))
totalWordNum = 0
while True:
    searchword = input("검색 할 문자열을 입력하세요.")    # 검색할 단어 입력
    for a in range(len(englishLine)):                   # a는 입력받은 문자열(문장)이 몇개인지
        temp = []                                       # 임시로 문자열의 원소의 원소(하나하나 알파벳)저장할 리스트
        stringCount = 0
        for b in englishLine[a]:                        # b는 문자열 각각 의 알파벳
            count = 0
            if b == " ":
                                                        # 공백이 나왔으므로
                                                        # 이전까지의 단어와 검색하려는 단어 비교
                if len(temp) == len(searchword):        # 일단 알파벳수가같은지
                    for c in range(len(temp)):          # C는 알파벳의 개수
                        if temp[c] == searchword[c]:    # 알파벳 같을때마다  
                            count +=1                   # 카운트추가
                    if count == len(temp):              # 단어길이도같고 원소도같음
                                                        # 같은 단어라는뜻
                        searchedCount += 1
                        if a not in searchedLine:       # a번째줄에 단어가 있으면
                            searchedLine.append(a)      # a를 검색된라인리스트에 추가
                stringCount +=1
                temp=[]        
            else:                                       # 공백이 아니면 실행 (문자열이라는뜻)
                if temp == []:                          # 앞에가 공백 혹은 문장의 시작이라면 단어수에 추가
                    totalWordNum += 1
                temp.append(b)                          # 알파벳을 temp에 저장
                stringCount +=1
                if stringCount == len(englishLine[a]):  # 마지막번째면
                    if len(temp) == len(searchword):    # 일단 알파벳수가같은지
                        for c in range(len(temp)):      # C는 알파벳의 개수
                            if temp[c] == searchword[c]:# 알파벳 같을때마다  
                                count +=1               # 카운트추가
                        if count == len(temp):          # 단어길이도같고 원소도같음
                                                        # 같은 단어라는뜻
                            searchedCount += 1
                            if a not in searchedLine:   # a번째줄에 단어가 있으면
                                searchedLine.append(a+1)# a+1(a는 0부터시작해서)
    if searchedLine == []:                              # 검색된 라인이 없으면
        print("찾을 수가 없습니다.",end='')              # 다시 검색할 문자열 입력받기
    else:
        break
print(searchword, "를 찾았습니다")
print("검색된 라인 수 : ",end='')
for a in searchedLine:
    print(a+1," ",end = '')
print("\n검색된 횟수 : ",searchedCount)
print("총 단어 수 : ",totalWordNum)

#코딩시간 총 7시간 이상 ㅋㅋㅋㅋㅋㅋㅋ