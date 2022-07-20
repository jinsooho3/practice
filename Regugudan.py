while True:
    print("-------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-------------------")
    menuNum= int(input(""))
    if menuNum == 1:
        print("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력")
        while True:
            danNum = int(input(""))
            if danNum >= 2 and danNum <= 9:
                for gobsem in range(1,10):
                    print(danNum, " X ",gobsem, " = ",danNum * gobsem )
            else:
                print("2~9사이 정수를 입력해주세요")
                continue
            break

    
    elif menuNum == 2:
        print("이용해주셔서 감사합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue