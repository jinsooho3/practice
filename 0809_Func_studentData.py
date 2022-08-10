# 기존자료에서 참고한 출력 함수
def outputData(**a):
    for k, v in a.items():
        print(k,":", v,"",end = '')
    print()

# 직접 만들어본 출력 함수
def newOutputData(argListA, argListB):
    for a in range(len(argListA)):
            print("[",end='')
            for b in range(len(argListB)):
                # 평균값의 소수점 첫번째 자리까지만 출력
                if b == 6:
                    print(argListB[b], round(argListA[a][b], 1),end=' ')
                else:
                    print(argListB[b], argListA[a][b],end=' ')
            print()

# 학생정보 입력 함수
def insertData():
    stdId = input("학번을 입력하세요: ")
    stdName = input("이름을 입력하세요: ")
    stdKor = int(input("국어 성적을 입력하세요: "))
    stdEng = int(input("영어 성적을 입력하세요: "))
    stdMath = int(input("수학 성적을 입력하세요: "))
    stdSum = stdKor + stdEng + stdMath
    stdAvg = stdSum / 3
    return stdId, stdName, stdKor, stdEng, stdMath, stdSum, stdAvg

# 메뉴출력 함수
def menu():
    print("=" * 20)
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력순)")
    print(" 3. 프로그램 종료","\n")
    print("현 입력데이터 갯수 : ", len(totalList))
    print("전체 학생 평균 값 : ",round(totalAvg, 2))
    print("=" * 20)
#############################################################

totalList = []
totalAvg = 0.0
dataName = ["id :","name :","kor :","eng :","math :","sum :","avg :"]
while True:
    menu()
    inputNum = int(input())
    if inputNum == 1:
        stdDataList = []
        for index in insertData():
            stdDataList.append(index)
        totalList.append(stdDataList)

        avgSum = 0
        for count in range(len(totalList)):
            avgSum += totalList[count][6]
        totalAvg = avgSum / len(totalList)


    if inputNum ==2:
        newOutputData(totalList, dataName)
        # 아래는 자료에서 만든 출력함수를 사용
        # for a in range(len(totalList)):
        #     print("[",end='')
        #     outputData(id = totalList[a][0], name = totalList[a][1], kor = totalList[a][2], eng = totalList[a][3], math = totalList[a][4], sum = totalList[a][5], avg =  totalList[a][6])
    if inputNum == 3:
        print("프로그램 종료")
        break