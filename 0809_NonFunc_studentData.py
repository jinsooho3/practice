totalList = []
totalAvg = 0.0
dataName = ["id :","name :","kor :","eng :","math :","sum :","avg :"]
while True:
    print("=" * 20)
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력순)")
    print(" 3. 프로그램 종료","\n")
    print("현 입력데이터 갯수 : ", len(totalList))
    print("전체 학생 평균 값 : ",totalAvg)
    print("=" * 20)
    inputNum = int(input())
    if inputNum == 1:
        stdDataList = []
        stdDataList.append(input("학번을 입력하세요: "))
        stdDataList.append(input("이름을 입력하세요: "))
        stdDataList.append(int(input("국어 성적을 입력하세요: ")))
        stdDataList.append(int(input("영어 성적을 입력하세요: ")))
        stdDataList.append(int(input("수학 성적을 입력하세요: ")))
        stdDataList.append(stdDataList[2] + stdDataList[3] + stdDataList[4])
        stdDataList.append(stdDataList[5] / 3)
        totalList.append(stdDataList)
        avgSum = 0
        for count in range(len(totalList)):
            avgSum += totalList[count][6]
        totalAvg = avgSum / len(totalList)
    if inputNum ==2:
        for a in range(len(totalList)):
            print("[",end='')
            for b in range(len(dataName)):
                print(dataName[b], totalList[a][b],end=' ')
            print()
    if inputNum == 3:
        print("프로그램 종료")
        break