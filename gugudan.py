while True:
#메뉴 출력
    print("----------------")
    print("1.구구단 출력")
    print("2. 프로그램 종료")
    print("----------------")
#키보드로 부터 정수값 입력받기
    menuNum = int(input(""))
#메뉴 1 선택시 구구단출력, 2인경우 msg출력후 프로그램종료
    if menuNum == 1:
        #1입력후 구구단 출력 메뉴 선택시 출력할 단을 입력받기
        #출력 유효단은 2~9
        # 2~9 이외의 값이 들어올경우 에러 메시지출력후 재입력
        print("출력할 구구단의 단을 입력하세요. 구구단의 단을 2~9사이 입력")
        while True:
            danNum = int(input(""))
            if danNum >=2 and danNum<=9:
                for gobsem in range(1,10):
                    print(danNum, " X ",gobsem," = ",danNum*gobsem)
                break
            else:
                print("2~9사이 정수를 입력해주세요")           
    elif menuNum ==2:
        print("이용해주셔서 감사합니다.")
        break
#메뉴에서 1,2 이외의 값이 입력될경우 에러msg 출력후 재입력받기
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue